from fastapi import FastAPI

from controller import book_controller

app = FastAPI()


app.include_router(book_controller.route)