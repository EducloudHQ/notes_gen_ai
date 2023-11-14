from aws_lambda_powertools import Logger, Tracer
import boto3
import os


from botocore.exceptions import ClientError

dynamodb = boto3.resource("dynamodb")
logger = Logger(service="get_notes_resolver")

table = dynamodb.Table(os.environ["NOTES_TABLE"])


def get_notes(userId:str):
    #write a method to query data from dynamodb with PK equal to USER#{userId} and SK begins with NOTES#
    try:
        response = table.query(
            KeyConditionExpression="PK = :pk and begins_with(SK, :sk)",
            ExpressionAttributeValues={
                ":pk": f"USER#{userId}",
                ":sk": "NOTE#"
            },
            ScanIndexForward=False
        )
        return response["Items"]

    except ClientError as e:
        logger.error(e)
        return []



