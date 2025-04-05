from sqlmodel import Session, select

from config.database import engine
from models.book import Book


class Book_Repository:
    __session = None
    
    def __init__(self):
        self.__session = Session(bind=engine)
    
    def get_all_books(self):
        return self.__session.exec(select(Book)).all()
    
    def get_a_book(self, book_id:int):
        return self.__session.exec(select(Book).where(Book.id==book_id)).first()

    def create_a_book(self, new_book:Book):
        self.__session.add(new_book)
        self.__session.commit()
        return new_book
    
    def update_a_book(self, book:Book):
        return self.create_a_book(book)
    
    def delete_a_book(self, book:Book):
        return self.__session.delete(book)