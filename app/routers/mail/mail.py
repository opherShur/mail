from fastapi import APIRouter

from app.models.letter import Letter
from app.routers.mail.utilities.letter_file_utilities import write_letter_to_file, read_letter_file, delete_letter_file

router = APIRouter()


@router.get('/read_letter/{letter_id}')
def get_letter(letter_id: str):
    return read_letter_file(letter_id)


@router.post('/write_letter')
def write_letter(letter: Letter):
    write_letter_to_file(letter)


@router.delete('/delete_letter/{letter_id}')
def delete_letter(letter_id: str):
    delete_letter_file(letter_id)
