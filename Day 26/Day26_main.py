from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# In-memory "database"
books_db = []

# Pydantic model for book
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

# Root route
@app.get("/")
def welcome():
    return {"message": "📚 Welcome to the Library API!"}

# Get all books
@app.get("/books", response_model=List[Book])
def get_books():
    return books_db

# Get a book by ID
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# Add a new book
@app.post("/books", response_model=Book)
def create_book(book: Book):
    for existing in books_db:
        if existing.id == book.id:
            raise HTTPException(status_code=400, detail="Book with this ID already exists")
    books_db.append(book)
    return book

# Update a book
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books_db):
        if book.id == book_id:
            books_db[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

# Delete a book
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books_db):
        if book.id == book_id:
            books_db.pop(index)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")
