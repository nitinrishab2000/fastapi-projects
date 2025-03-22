from fastapi import Body, FastAPI

app = FastAPI()


books = [
    {"title": "Title One", "author": "Author One", "category": "Science"},
    {"title": "Title Two", "author": "Author One", "category": "Science"},
    {"title": "Title Three", "author": "Author Two", "category": "Fiction"},
    {"title": "Title Four", "author": "Author Two", "category": "Fiction"},
    {"title": "Title Five", "author": "Author Three", "category": "History"},
    {"title": "Title Six", "author": "Author Three", "category": "History"},
    {"title": "Title Seven", "author": "Author Four", "category": "Technology"},
    {"title": "Title Eight", "author": "Author Four", "category": "Technology"},
    {"title": "Title Nine", "author": "Author Five", "category": "Philosophy"},
    {"title": "Title Ten", "author": "Author Five", "category": "Philosophy"},
    {"title": "Title Eleven", "author": "Author Six", "category": "Self-Help"},
    {"title": "Title Twelve", "author": "Author Six", "category": "Self-Help"},
    {"title": "Title Thirteen", "author": "Author Seven", "category": "Math"},
    {"title": "Title Fourteen", "author": "Author Seven", "category": "Math"},
    {"title": "Title Fifteen", "author": "Author One", "category": "Science"},
]

@app.get("/books/author/")
async def get_books_by_author_using_query_parameter(author_name:str):
    books_to_return = []
    for i in range(len(books)):
       if(books[i].get("author").casefold()==author_name.casefold()):
           books_to_return.append(books[i])
            ##books_to_return.append({books[i].get("author").casefold():author_name.casefold()})
    return books_to_return


@app.get("/books/author/{author_name}")
async def get_books_by_author(author_name:str):
    books_to_return = []
    for i in range(len(books)):
       if(books[i].get("author").casefold()==author_name.casefold()):
           books_to_return.append(books[i])
            ##books_to_return.append({books[i].get("author").casefold():author_name.casefold()})
    return books_to_return

@app.delete("/books/delete/delete_book/{book_title}")
async def delete_book(book_title:str):
    for i in range(len(books)):
        if(books[i].get('title').casefold()==book_title.casefold()):
            books.pop(i)
            break

@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(books)):
        if(books[i].get('title').casefold()==updated_book.get('title').casefold()):
            books[i] = updated_book

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    books.append(new_book)

@app.get("/books")
async def read_all_books():
    return books

## Both query and path parameter

@app.get("/books/{title_name}/")
async def read_books(category:str,title_name:str):
    books_to_return = []
    for book in books:
        if book.get('title').casefold()==title_name.casefold() and book.get('category').casefold()==category.casefold():
            books_to_return.append(book)
        
    return books_to_return


## Query Parameter

# @app.get("/books/")
# async def read_books(category:str):
#     books_to_return = []
#     for book in books:
#         if book.get('category').casefold() == category.casefold():
#             books_to_return.append(book)
    
#     return books_to_return


# @app.get("/books/{book_title}")
# async def read_book(book_title):
#     for book in books:
#         if book.get('title').casefold() == book_title.casefold():
#             return book

# @app.get("/books/mybook")
# async def read_my_books():
#     return {"My Favourite book":'My Favourite Book'}

# @app.get("/books/{dynamic_param}")
# async def read_dynamic_books(dynamic_param):
#     return {"dynamic_param":dynamic_param}

