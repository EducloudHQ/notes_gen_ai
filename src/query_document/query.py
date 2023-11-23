import json

import boto3
from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler.appsync import Router
from botocore.exceptions import ClientError

from langchain.llms.bedrock import Bedrock

from langchain.embeddings import BedrockEmbeddings
from momento import (
    CredentialProvider,
    PreviewVectorIndexClient,
    VectorIndexConfigurations,
)

from langchain.vectorstores import MomentoVectorIndex
from langchain.chains import (
    RetrievalQA
)



s3 = boto3.client("s3")
logger = Logger()


logger = Logger(child=True)
router = Router()
def get_secret():
    secret_name = "dev/notes_api/momento"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']
    return secret


@router.resolver(type_name="Query", field_name="queryDocument")
def query_document(input:str):

    bedrock_runtime = boto3.client(
        service_name="bedrock-runtime",
        region_name="us-east-1",
    )

    secret = get_secret()
    momento_api_key = json.loads(secret)


    embeddings, llm = BedrockEmbeddings(
        model_id="amazon.titan-embed-text-v1",
        client=bedrock_runtime,
        region_name="us-east-1",
    ), Bedrock(
        model_id="anthropic.claude-v2", client=bedrock_runtime, region_name="us-east-1"
    )
    api_key = momento_api_key['MOMENTO_API_KEY']
    vector_db = MomentoVectorIndex(embedding=embeddings,
                                   client=PreviewVectorIndexClient(
                                       VectorIndexConfigurations.Default.latest(),
                                       credential_provider= CredentialProvider.from_string(api_key),
                                   ),

                                   index_name="summary")

    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vector_db.as_retriever(),
                                           )

    res = qa_chain({"query": input})

    logger.info(f"result is ${res}")

    return {"result":res['result'] .replace("\n", "")}
