from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler.appsync import Router
from user import create_user_account as createUserAccount

logger = Logger(child=True)
router = Router()


@router.resolver(type_name="Mutation", field_name="createUserAccount")
def create_user(user=None):
    if user is None:
        user = {}
    return createUserAccount(user)
