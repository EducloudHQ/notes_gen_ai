from aws_lambda_powertools import Logger, Tracer
import boto3
import os

from decimal import *
from aws_lambda_powertools.utilities.data_classes.appsync import scalar_types_utils
from botocore.exceptions import ClientError

dynamodb = boto3.resource("dynamodb")

logger = Logger(service="create_note")
tracer = Tracer(service="create_note")

table = dynamodb.Table(os.environ["NOTES_TABLE"])


# https://stackoverflow.com/questions/63026648/errormessage-class-decimal-inexact-class-decimal-rounded-while
@tracer.capture_method
def create_note(notesInput=None):
    if notesInput is None:
        notesInput = {}
    item = {
        "id": scalar_types_utils.make_id(),
        "note": notesInput["note"],
        "title": notesInput["title"],
        "status": True,
        "username": notesInput["username"],
        "createdOn":scalar_types_utils.aws_timestamp()

    }

    logger.info(" create note item {}".format(item))

    try:

        response = table.put_item(
            Item={
                "PK": f"USER#{item['username']}",
                "SK": f"NOTE#{item['id']}",
                "GSI1PK": f"NOTE#{item['id']}",
                "GSI1SK": f"NOTE#METADATA",

                **item,
            }
        )

        logger.info(" create note response {}".format(response))
        return item

    except ClientError as err:
        logger.debug(f"Error occurred during note creation {err.response['Error']}")
        raise err
