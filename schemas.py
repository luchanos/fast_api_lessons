from pydantic import BaseModel, validator
from datetime import date
from typing import List


class Genre(BaseModel):
    name: str


class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre]
    pages: int


class BookOut(Book):
    id: int


class Author(BaseModel):
    first_name: str
    last_name: str
    age: int

    @validator("age")
    def check_age(cls, v):
        if v < 15:
            raise ValueError("Cannot be less than 15!")
        return v
