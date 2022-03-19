from fastapi import FastAPI
import uvicorn

from letter import Letter
from letter_file_utilities import write_letter_to_file, read_letter_file

app = FastAPI()
