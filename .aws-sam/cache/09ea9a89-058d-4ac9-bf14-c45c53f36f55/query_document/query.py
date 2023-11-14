import boto3
from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler.appsync import Router

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


@router.resolver(type_name="Query", field_name="queryDocument")
def query_document(input:str):

    bedrock_runtime = boto3.client(
        service_name="bedrock-runtime",
        region_name="us-east-1",
    )

    embeddings, llm = BedrockEmbeddings(
        model_id="amazon.titan-embed-text-v1",
        client=bedrock_runtime,
        region_name="us-east-1",
    ), Bedrock(
        model_id="anthropic.claude-v2", client=bedrock_runtime, region_name="us-east-1"
    )

    vector_db = MomentoVectorIndex(embedding=embeddings,
                                   client=PreviewVectorIndexClient(
                                       VectorIndexConfigurations.Default.latest(),
                                       credential_provider=CredentialProvider.from_environment_variable(
                                           "MOMENTO_API_KEY"
                                       ),
                                   ),

                                   index_name="summary")

    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vector_db.as_retriever(),
                                           )

    res = qa_chain({"query": input})

    logger.info(f"result is ${res}")

    return {"result":res['result'] .replace("\n", "")}
