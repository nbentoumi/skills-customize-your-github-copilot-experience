from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Mergington Book API")


class BookCreate(BaseModel):
    title: str
    author: str
    year: int


books = {
    1: {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    2: {"id": 2, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle", "year": 1962},
}


@app.get("/")
def read_root():
    return {"message": "Welcome to the Mergington Book API"}


# TODO: Add GET /books and GET /books/{book_id} endpoints.


# TODO: Add POST /books and PUT /books/{book_id} endpoints.


# TODO: Add DELETE /books/{book_id} and tests for the API.
