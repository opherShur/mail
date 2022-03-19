from pathlib import Path
from uuid import UUID

from letter import Letter
from consts import LetterConsts


def write_letter(letter: Letter):
    """
    Receive letter object and write it to file.
    Assumes it doesn't exist.
    :param letter: letter object
    """
    letter_path = create_letter_path(letter)
    with open(letter_path) as letter_file:
        letter_file.write(letter.json())


def read_letter(letter_id: UUID) -> Letter:
    """
    Get a letter uuid, and return a letter object
    :param letter_id: uuid of letter
    :return: letter object as taken from saved letter
    """
    letter_path = get_letter_path(letter_id)
    return Letter.parse_file(letter_path)


def create_letter_path(letter: Letter) -> Path:
    """
    Receive letter object and return its path (based on its ID)
    :param letter: letter object
    :return: path to letter
    """
    return LetterConsts.LETTER_BASE_PATH + letter.id + LetterConsts.LETTER_FILE_EXTENSION


def get_letter_path(letter_id: UUID):
    """
    Receive letter id and return its path (based on its ID)
    :param letter_id: letter uuid
    :return: path to letter
    """
    return LetterConsts.LETTER_BASE_PATH + str(letter_id) + LetterConsts.LETTER_FILE_EXTENSION
