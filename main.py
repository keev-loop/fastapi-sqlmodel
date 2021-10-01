from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from models import Book
from database import engine
from sqlmodel import Session, select
from typing import Optional, List


app=FastAPI()
session=Session(bind=engine)


@app.get('/books', response_model=List[Book], status_code=status.HTTP_200_OK)
async def get_all_books():
    statement = select(Book)
    result = session.exec(statement).all()
    return result


@app.get('/book/{book_id}', response_model=Book, status_code=status.HTTP_200_OK)
async def get_a_book(book_id:int):
    statement = select(Book).where(Book.id==book_id)
    result = session.exec(statement).first()
    
    if result == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return result


@app.post('/books', response_model=Book, status_code=status.HTTP_201_CREATED)
async def create_an_book(book:Book):
    new_book = Book(
        title=book.title,
        description=book.description,
    )
    session.add(new_book)
    session.commit()
    return new_book


@app.put('/book/{book_id}', response_model=Book, status_code=status.HTTP_200_OK)
async def create_an_book(book_id:int, new_book:Book):
    statement = select(Book).where(Book.id==book_id)
    book = session.exec(statement).first()

    if book == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    book.title = new_book.title
    book.description = new_book.description
    
    session.commit()
    return book


@app.delete('/book/{book_id}', status_code=status.HTTP_200_OK)
async def delete_an_book(book_id:int):
    statement = select(Book).where(Book.id==book_id)
    result = session.exec(statement).one_or_none()
    
    if result == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
    
    session.delete(result)

    return result

