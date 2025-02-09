from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List

books = [
    {
        "id": 1,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "publisher": "Prentice Hall",
        "published_date": "2008-08-11",
        "page_count": 464,
        "language": "English",
    },
    {
        "id": 2,
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt, David Thomas",
        "publisher": "Addison-Wesley",
        "published_date": "1999-10-30",
        "page_count": 352,
        "language": "English",
    },
    {
        "id": 3,
        "title": "Introduction to the Theory of Computation",
        "author": "Michael Sipser",
        "publisher": "Cengage Learning",
        "published_date": "2012-06-27",
        "page_count": 504,
        "language": "English",
    },
    {
        "id": 4,
        "title": "Design Patterns: Elements of Reusable Object-Oriented Software",
        "author": "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides",
        "publisher": "Addison-Wesley",
        "published_date": "1994-10-21",
        "page_count": 395,
        "language": "English",
    },
    {
        "id": 5,
        "title": "You Don't Know JS",
        "author": "Kyle Simpson",
        "publisher": "O'Reilly Media",
        "published_date": "2014-12-27",
        "page_count": 278,
        "language": "English",
    },
    {
        "id": 6,
        "title": "Eloquent JavaScript",
        "author": "Marijn Haverbeke",
        "publisher": "No Starch Press",
        "published_date": "2018-12-04",
        "page_count": 472,
        "language": "English",
    },
    {
        "id": 7,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "publisher": "No Starch Press",
        "published_date": "2015-11-01",
        "page_count": 560,
        "language": "English",
    },
    {
        "id": 8,
        "title": "Artificial Intelligence: A Modern Approach",
        "author": "Stuart Russell, Peter Norvig",
        "publisher": "Pearson",
        "published_date": "2020-04-28",
        "page_count": 1152,
        "language": "English",
    },
    {
        "id": 9,
        "title": "Deep Learning",
        "author": "Ian Goodfellow, Yoshua Bengio, Aaron Courville",
        "publisher": "MIT Press",
        "published_date": "2016-11-18",
        "page_count": 800,
        "language": "English",
    },
    {
        "id": 10,
        "title": "Computer Networking: A Top-Down Approach",
        "author": "James F. Kurose, Keith W. Ross",
        "publisher": "Pearson",
        "published_date": "2020-03-04",
        "page_count": 864,
        "language": "English",
    },
]

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


class BookUpdate(BaseModel):
    title: str
    author: str
    language: str
    publisher: str
    page_count: int


@app.get("/books", response_model=List[Book])
async def get_all_books():
    return books


@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_book(book: Book) -> dict:
    new_book = book.model_dump()
    books.append(new_book)
    return new_book


@app.get("/book/{book_id}")
async def get_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.patch("/book/{book_id}")
async def update_book(book_id: int, book_data: BookUpdate) -> dict:
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_data.title
            book["author"] = book_data.author
            book["language"] = book_data.language
            book["page_count"] = book_data.page_count
            book["publisher"] = book_data.publisher

            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.delete("/book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)

            return {}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
