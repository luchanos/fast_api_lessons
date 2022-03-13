from fastapi import FastAPI, Query, Path, Body
from schemas import Book, Author, BookOut

app = FastAPI()


@app.get("/")
def home():
    return {"key": "hello"}


# @app.get("/{pk}")
# def get_item(pk: int, q: float = None):
#     return {"key": pk, "q": q}


# @app.get("/user/{pk}/items/{item}")
# def get_user_item(pk: int, item: str):
#     return {"user": pk, "item": item}


@app.post("/book")
def create_book(item: Book, author: Author, quantity: int = Body(...)):
    return {"item": item, "author": author, "quantity": quantity}


@app.post("/second_book", response_model=BookOut)
def create_book(item: Book):
    return BookOut(**item.dict(), id=123)


@app.get("/book")
def get_book(q: str = Query(..., min_length=5, max_length=10, description="search book")):
    return q


@app.get("/book/{pk}")
def get_item(pk: int = Path(..., gt=1)):
    return {"key": pk}
