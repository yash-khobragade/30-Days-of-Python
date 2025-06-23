from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# SQLite DB setup
DATABASE_URL = "sqlite:///./books.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# SQLAlchemy model
class BookModel(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=False)

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic schema
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

    class Config:
        orm_mode = True

# FastAPI app
app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root route
@app.get("/")
def welcome():
    return {"message": "📚 Welcome to the Library API!"}

# Get all books
@app.get("/books", response_model=List[Book])
def get_books(db: Session = Depends(get_db)):
    books = db.query(BookModel).all()
    return books

# Get book by ID
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# Add a book
@app.post("/books", response_model=Book)
def create_book(book: Book, db: Session = Depends(get_db)):
    existing = db.query(BookModel).filter(BookModel.id == book.id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Book with this ID already exists")

    db_book = BookModel(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Update a book
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    book.title = updated_book.title
    book.author = updated_book.author
    book.year = updated_book.year

    db.commit()
    db.refresh(book)
    return book

# Delete a book
@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully"}
