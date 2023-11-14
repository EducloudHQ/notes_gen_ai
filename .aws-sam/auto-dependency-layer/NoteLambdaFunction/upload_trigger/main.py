import os, json
from datetime import datetime
import boto3
from pypdf import PdfReader
import shortuuid
import urllib
from aws_lambda_powertools import Logger

DOCUMENT_TABLE = os.environ["DOCS_TABLE"]
QUEUE = os.environ["QUEUE"]
BUCKET = os.environ["BUCKET"]


ddb = boto3.resource("dynamodb")
document_table = ddb.Table(DOCUMENT_TABLE)
sqs = boto3.client("sqs")
s3 = boto3.client("s3")
logger = Logger()


@logger.inject_lambda_context(log_event=True)
def lambda_handler(event, context):
    key = urllib.parse.unquote_plus(event["Records"][0]["s3"]["object"]["key"])
    split = key.split("/")
    user_id = split[1]
    file_name = split[2]
    logger.info(f"key is {key}")

    document_id = shortuuid.uuid()

    s3.download_file(BUCKET, key, f"/tmp/{file_name}")

    with open(f"/tmp/{file_name}", "rb") as f:
        reader = PdfReader(f)
        pages = str(len(reader.pages))

    conversation_id = shortuuid.uuid()

    timestamp = datetime.utcnow()
    timestamp_str = timestamp.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    document = {
        "userId": user_id,
        "documentId": document_id,
        "filename": file_name,
        "created": timestamp_str,
        "pages": pages,
        "filesize": str(event["Records"][0]["s3"]["object"]["size"]),
        "docstatus": "UPLOADED",
        "conversations": [],
    }

    logger.debug("this is it:")

    logger.info(document)

    conversation = {"conversationId": conversation_id, "created": timestamp_str}
    document["conversations"].append(conversation)

    document_table.put_item(Item=document)



    message = {
        "documentId": document_id,
        "key": key,
        "user": user_id,
    }
    sqs.send_message(QueueUrl=QUEUE, MessageBody=json.dumps(message))
