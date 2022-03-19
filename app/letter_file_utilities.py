from pathlib import Path
from os import remove

from app.models.letter import Letter
from consts import LetterConsts


def write_letter_to_file(letter: Letter):
    """
    Receive letter object and write it to file.
    Assumes it doesn't exist.
    :param letter: letter object
    """
    letter_path = create_letter_path(letter)
    with open(letter_path, "w") as letter_file:
        letter_file.write(letter.json())


def read_letter_file(letter_id: str) -> Letter:
    """
    Get a letter uuid, and return a letter object
    :param letter_id: uuid of letter as string
    :return: letter object as taken from saved letter
    """
    letter_path = get_letter_path(letter_id)
    return Letter.parse_file(letter_path)


def delete_letter_file(letter_id: str):
    """
    Get letter uuid and delete it
    :param letter_id: uuid of letter as string
    """
    letter_path = get_letter_path(letter_id)
    remove(letter_path)


def create_letter_path(letter: Letter) -> Path:
    """
    Receive letter object and return its path (based on its ID)
    :param letter: letter object
    :return: path to letter
    """
    return LetterConsts.LETTER_BASE_PATH / (str(letter.id) + LetterConsts.LETTER_FILE_EXTENSION)


def get_letter_path(letter_id: str) -> Path:
    """
    Receive letter id and return its path (based on its ID)
    :param letter_id: letter uuid as string
    :return: path to letter
    """
    return LetterConsts.LETTER_BASE_PATH / (str(letter_id) + LetterConsts.LETTER_FILE_EXTENSION)
