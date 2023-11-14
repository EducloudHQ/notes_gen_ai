from aws_lambda_powertools import Logger, Tracer
import boto3
import os

from botocore.exceptions import ClientError

dynamodb = boto3.resource("dynamodb")
tracer = Tracer(service="get_note")
logger = Logger(service="get_note")

table = dynamodb.Table(os.environ["NOTES_TABLE"])


@tracer.capture_method
def get_note(userId: str, id: str):
    logger.debug(f"note id is:{id}")

    try:
        response = table.get_item(
            Key={"PK": f"USER#{userId}", "SK": f"NOTE#{id}"}
        )
        logger.debug("notes dict {}".format(response))
        if response["Item"] is None:
            logger.debug("response is null")
            return {}
        else:
            result = response["Item"]
            logger.debug(f"response is not {result}")

            return result

    except ClientError as err:
        logger.debug(f"Error occurred during get note i {err.response['Error']}")
        raise err
