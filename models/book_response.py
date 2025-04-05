from pydantic import BaseModel

from models.book import Book


class Book_Response(BaseModel):
    title: str | None = None
    description: str | None = None
    
    def __init__(self, title, description):
        self.title = title
        self.description = description
    
    def __init__(self, book:Book):
        self.title = book.title
        self.description = book.description