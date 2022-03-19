from fastapi import FastAPI
import uvicorn

from app.routers.mail import mail

app = FastAPI()

app.include_router(mail.router, prefix='/mail')

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)
