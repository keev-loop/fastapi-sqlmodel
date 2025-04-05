from pydantic import BaseModel

from models.book import Book


class Book_Request(BaseModel):
    title: str | None = None
    description: str | None = None
    
    def toEntity(self):
        return Book(title=self.title, description=self.description)