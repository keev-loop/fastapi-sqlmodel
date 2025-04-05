from typing import List

from fastapi import APIRouter, status

from models.book_request import Book_Request
from models.book_response import Book_Response
from service.book_service import Book_Service

route = APIRouter()
_service = Book_Service()

class Book_Controller:
    def __init__():
        pass
        
    @route.get('/books', response_model=List[Book_Response], status_code=status.HTTP_200_OK)
    def get_all_books():
        return _service.get_all_books()
    

    @route.get('/book/{book_id}', status_code=status.HTTP_200_OK)
    def get_a_book(book_id:int):
        return _service.get_a_book(book_id)


    @route.post('/book', response_model=Book_Response, status_code=status.HTTP_201_CREATED)
    def create_a_book(book:Book_Request):
        return _service.create_a_book(book)


    @route.put('/book/{book_id}', response_model=Book_Response, status_code=status.HTTP_200_OK)
    def update_a_book(book_id:int, new_book:Book_Request):
        return _service.update_a_book(book_id, new_book)


    @route.delete('/book/{book_id}', status_code=status.HTTP_200_OK)
    def delete_a_book(book_id:int):
        return _service.delete_a_book(book_id)