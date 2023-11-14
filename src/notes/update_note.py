from aws_lambda_powertools import Logger, Tracer
import boto3
import os

from decimal import *
from aws_lambda_powertools.utilities.data_classes.appsync import scalar_types_utils
from botocore.exceptions import ClientError

dynamodb = boto3.resource("dynamodb")

logger = Logger(service="update_note")
tracer = Tracer(service="update_note")

table = dynamodb.Table(os.environ["NOTES_TABLE"])


# https://stackoverflow.com/questions/63026648/errormessage-class-decimal-inexact-class-decimal-rounded-while
@tracer.capture_method
def update_note(notesInput=None):
    if notesInput is None:
        notesInput = {}
    item = {
        "id": notesInput["id"],
        "note": notesInput["note"],
        "title": notesInput["title"],
        "username": notesInput["username"],
        "status": notesInput["status"],
        "updatedOn":scalar_types_utils.aws_timestamp()

    }

    logger.info("update note item {}".format(item))


    try:
        response = table.update_item(
            Key={"PK": f'USER#{item["username"]}', "SK": f'NOTE#{item["id"]}'},
            ConditionExpression="attribute_exists(PK)",
            UpdateExpression="set title= :title, note = :note,#status= :status,updatedOn= :updatedOn",
            ExpressionAttributeNames={
                "#status": "status",
            },
            ExpressionAttributeValues={
                ":note": item["note"],
                ":title": item["title"],
                ":status": item["status"],
                ":updatedOn": item["updatedOn"]

            },
            ReturnValues="ALL_NEW",
        )

        logger.debug({" update response": response["Attributes"]})
        return response["Attributes"]

    except ClientError as err:
        logger.debug(f"Error occurred during note update{err.response['Error']}")
        raise err


