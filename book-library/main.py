from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

app = FastAPI()
books = {}

@app.post("/books/")
def create_book(title: str, author: str, year: int):
    book_id = max(books.keys()) + 1 if books else 1
    book = Book(id=book_id, title=title, author=author, year=year)
    for tempBook in books.values():
        if tempBook.title == title and tempBook.author == author and tempBook.year == year:
            raise HTTPException(status_code=400, detail="This book already exists.")
    books[book_id] = book
    return book

@app.get("/books/")
def read_books():
    return list(books.values())

@app.get("/books/{id}")
def read_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found.")
    return books[book_id]

@app.put("/books/{id}")
def update_book(book_id: int, title: str = None, author: str = None, year: int = None):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found.")
    book = books[book_id]
    if title is not None:
        book.title = title
    if author is not None:
        book.author = author
    if year is not None:
        book.year = year
    return book

@app.delete("/books/{id}")
def delete_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found.")
    del books[book_id]
    return {"detail": "Book deleted successfully."}

