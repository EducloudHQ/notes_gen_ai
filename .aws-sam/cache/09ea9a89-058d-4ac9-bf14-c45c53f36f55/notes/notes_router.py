from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler.appsync import Router
from notes.create_note import create_note
from notes.update_note import update_note
from notes.get_note import get_note
from notes.get_notes import get_notes
from notes.enhance_note import enhance_note


logger = Logger(child=True)
router = Router()


@router.resolver(type_name="Mutation", field_name="createNote")
def create_notes(notesInput=None):
    if notesInput is None:
        notesInput = {}
    return create_note(notesInput)

@router.resolver(type_name="Mutation", field_name="updateNote")
def update_notes(notesInput=None):
    if notesInput is None:
        notesInput = {}
    return update_note(notesInput)

@router.resolver(type_name="Query", field_name="getNote")
def get_a_note(userId:str,id:str):
    return get_note(userId,id)

@router.resolver(type_name="Query", field_name="getAllNotes")
def get_all_note(userId:str):
    return get_notes(userId)

@router.resolver(type_name="Query", field_name="enhanceNote")
def enhance_notes(input=None):
    if input is None:
        input = {}
    return enhance_note(input)
