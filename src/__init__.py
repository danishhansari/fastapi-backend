from fastapi import FastAPI
from src.books.route import book_router


version = "v1"
app = FastAPI(description="A rest api for a book review web service", version=version)

app.include_router(book_router, prefix="/api/{version}/books", tags=["books"])
