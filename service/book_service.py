from fastapi import status
from fastapi.exceptions import HTTPException

from models.book import Book
from models.book_request import Book_Request
from models.book_response import Book_Response
from repository.book_repository import Book_Repository


class Book_Service:
    __repository = None
    
    def __init__(self):
        self.__repository = Book_Repository()
        
    def get_all_books(self):
        print(self.__repository.get_all_books())
        return Book_Response(
            self.__repository.get_all_books())
    
    def get_a_book(self, book_id:int):
        book = self.__repository.get_a_book(book_id)
        
        if book is not None:
            return Book_Response(book)
        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    def create_a_book(self, book:Book_Request):
        print(book)
        new_book = book.toEntity()
        print(new_book)
        return Book_Response(
            self.__repository.create_a_book(new_book))
    
    def update_a_book(self, book_id:int, new_book:Book_Request):
        book = self.get_a_book(book_id)

        book.title = new_book.title
        book.description = new_book.description
        
        return Book_Response(
            self.__repository.update_a_book(book))
    
    def delete_a_book(self, book_id:int):
        book = self.get_a_book(book_id)

        return Book_Response(
            self.__repository.delete_a_book(book))