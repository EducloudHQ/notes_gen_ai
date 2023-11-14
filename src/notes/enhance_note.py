from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools import Metrics
from aws_lambda_powertools.metrics import MetricUnit
import json

from botocore.exceptions import ClientError
import boto3

logger = Logger(service="enhance_note")
tracer = Tracer(service="enhance_note")

metrics = Metrics(namespace="Powertools")

@tracer.capture_method
def enhance_note(input: str):
    # adding custom metrics
    # See: https://awslabs.github.io/aws-lambda-powertools-python/latest/core/metrics/
    global response_body
    metrics.add_metric(name="GenerativeAIInvocations", unit=MetricUnit.Count, value=1)
    bedrock_runtime = boto3.client(
        service_name="bedrock-runtime",
        region_name="us-east-1",
    )
    # create the prompt
    prompt_data = f"""
    Command: Please translate this text to french {input}"""

    body = json.dumps({
        "prompt": prompt_data,
        "maxTokens": 200,
        "stopSequences": [],
        "temperature": 0.7,
        "topP": 1,

    })

    modelId = 'ai21.j2-ultra-v1'
    accept = 'application/json'
    contentType = 'application/json'
    outputText = "\n"
    logger.debug(f"input: we in here")



    try:
        logger.debug(f"input: we in here")
        response = bedrock_runtime.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)

        response_body = json.loads(response.get('body').read())
        logger.debug(f"response body: {response_body}")

        outputText = response_body.get('completions')[0].get('data').get('text')



    except ClientError as error:

        if error.response['Error']['Code'] == 'AccessDeniedException':
            logger.debug(f"\x1b[41m{error.response['Error']['Message']}\
                    \nTo troubleshoot this issue please refer to the following resources.\
                     \nhttps://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_access-denied.html\
                     \nhttps://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html\x1b[0m\n")

        else:
            raise error

    return {"result":outputText.replace("\n", "")}

