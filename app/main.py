from fastapi import FastAPI
import uvicorn

from app.models.letter import Letter
from letter_file_utilities import write_letter_to_file, read_letter_file, delete_letter_file

app = FastAPI()


@app.get('/read_letter/{letter_id}')
def get_letter(letter_id: str):
    return read_letter_file(letter_id)


@app.post('/write_letter')
def write_letter(letter: Letter):
    write_letter_to_file(letter)


@app.delete('/delete_letter/{letter_id}')
def delete_letter(letter_id: str):
    delete_letter_file(letter_id)


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)
