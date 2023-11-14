from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler.appsync import Router
from notes.create_note import create_note
from notes.enhance_note import enhance_note


logger = Logger(child=True)
router = Router()


@router.resolver(type_name="Mutation", field_name="createNote")
def create_notes(notesInput=None):
    if notesInput is None:
        notesInput = {}
    return create_note(notesInput)


@router.resolver(type_name="Query", field_name="enhanceNote")
def enhance_notes(input=None):
    if input is None:
        input = {}
    return enhance_note(input)
