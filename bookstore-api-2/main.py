from fastapi import FastAPI,Body,Path, Query
from pydantic import BaseModel,Field
from typing import Optional
from fastapi import HTTPException
from starlette import status


app = FastAPI()


class Book:
    id:          int
    title:       str 
    author:      str
    description: str
    rating:      int
    published_date : int
    
    def __init__(self,id,title,author,description,rating,published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date
        
        
class BookRequest(BaseModel):
    id:              Optional[int] = Field(description="ID is not needed on create",default=None)
    title:           str = Field(min_length = 3)
    author:          str = Field(min_length = 1)
    description:     str = Field(min_length=1, max_length=100)
    rating:          int = Field(gt=0, lt=6)
    published_date : int = Field(gt=1999,lt=2031)
    
    model_config = {
        "json_schema_extra":{
            "example":{
                "title":"A new book",
                "author":"codingwithnitin",
                "description":"A new description",
                "rating":5,
                "published_date": 2000
            }
        }
    }

BOOKS = [
    Book(1, "Computer Science Pro", "Coding with Nitin", "A very nice book!", 5,2024),
    Book(2, "Mastering Python", "John Doe", "Comprehensive guide to Python programming.", 4,2029),
    Book(3, "AI for Beginners", "Jane Smith", "Introduction to Artificial Intelligence concepts.", 5,2012),
    Book(4, "Deep Learning with TensorFlow", "Andrew Ng", "Advanced deep learning techniques.", 5,2029),
    Book(5, "The Art of Problem Solving", "Paul Zeitz", "Techniques to improve problem-solving skills.", 4,2007),
    Book(6, "Software Engineering Principles", "Robert Martin", "Best practices for software development.", 5,2004)
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

 
# @app.post("/create-books")
# async def create_book(new_book = Body()):
#     BOOKS.append(new_book)

@app.post("/create-books", status_code=status.HTTP_201_CREATED)
async def create_book(book_request : BookRequest):
    new_book = Book(**book_request.model_dump())
    print(type(new_book))
    BOOKS.append(find_book_id(new_book))
    

def find_book_id(new_book:Book):
    if len(BOOKS)>0:
        new_book.id = BOOKS[-1].id+1
    else:
        new_book.id = 1
        
    return new_book

@app.get("/book/{book_id}", status_code=status.HTTP_200_OK)
async def read_book_by_id(book_id:int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
        
    raise HTTPException(status_code = 404, detail = 'Item not found')
    
@app.get("/book/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating:int = Query(gt=0,lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
            
    return books_to_return

@app.put("/book/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book:BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            return
    
    raise HTTPException(status_code=404,detail='Item not found')
            
@app.delete("/book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id:int = Path(gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            return
        
    raise HTTPException(status_code=404,detail='Item not found')
    
        
@app.get("/book/publish/", status_code=status.HTTP_200_OK)
async def read_books_by_publish_date(publish_date:int = Query(gt=1999,lt=2031)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == publish_date:
            books_to_return.append(book)
    
    return books_to_return
    
