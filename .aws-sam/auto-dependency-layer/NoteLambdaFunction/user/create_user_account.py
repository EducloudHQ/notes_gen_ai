from aws_lambda_powertools import Logger, Tracer
import boto3
import os

from aws_lambda_powertools.utilities.data_classes.appsync import scalar_types_utils
from botocore.exceptions import ClientError

tracer = Tracer(service="create_user_account")
logger = Logger(service="create_user_account")

client = boto3.client("dynamodb")

userTable = os.environ["USER_TABLE"]


@tracer.capture_method
def create_user_account(user=None):
    if user is None:
        user = {}
    logger.info(f"items:{user}")

    item: dict = {
        "id": scalar_types_utils.make_id(),
        "username": user["username"],
        "email": user["email"]
    }
    logger.debug(f"items:{item}")

    try:
        response = client.transact_write_items(
            TransactItems=[
                {
                    "Put": {
                        "Item": {
                            "PK": {"S": f'USER#{item["username"]}'},
                            "SK": {"S": f'USER#{item["username"]}'},
                            "id": {"S": item["id"]},
                            "username": {"S": item["username"]},

                            "email": {"S": item["email"]},

                            "createdOn": {"N": f"{scalar_types_utils.aws_timestamp()}"},
                        },
                        "TableName": userTable,
                        "ConditionExpression": "attribute_not_exists(PK)",
                    },
                },
                {
                    "Put": {
                        "Item": {
                            "PK": {"S": f'USEREMAIL#{item["email"]}'},
                            "SK": {"S": f'USEREMAIL#{item["email"]}'},
                            "id": {"S": item["id"]},
                            "username": {"S": item["username"]},
                            "email": {"S": item["email"]},
                        },
                        "TableName": userTable,
                        "ConditionExpression": "attribute_not_exists(PK)",
                    }
                },
            ]
        )
        tracer.put_annotation("CREATE_USER_TRANSACTION", "SUCCESS")
        logger.debug(f"transaction response is {response}")
        return item
    except ClientError as err:
        logger.debug(f"Error occurred during transact write{err.response}")
        logger.debug(f"Error occurred during transact write{err}")
        logger.debug(f"Error occurred during transact write{err.response['Error']}")
        if err.response["Error"]["Code"] == "TransactionCanceledException":
            if (
                err.response["CancellationReasons"][0]["Code"]
                == "ConditionalCheckFailed"
            ):
                # TODO make exception handling DRY
                errObj = Exception("Username already exist")

                raise errObj
            elif (
                err.response["CancellationReasons"][1]["Code"]
                == "ConditionalCheckFailed"
            ):
                # TODO make exception handling DRY
                errObj = Exception("Email already exist")

                raise errObj

        else:
            raise err
