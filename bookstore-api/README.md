# Bookstore API 📚

A simple **FastAPI**-based project that allows users to manage a collection of books. It supports CRUD operations such as **creating, reading, updating, and deleting books**.

## Features 🚀  
✅ Get all books  
✅ Get books by author (query & path parameters)  
✅ Get books by title and category  
✅ Create a new book  
✅ Update an existing book  
✅ Delete a book  


## Run the API ▶️  
Start the FastAPI server using Uvicorn:  
```
uvicorn main:app --reload
```
API will be accessible at:  
🔗 **http://127.0.0.1:8000**

## API Endpoints  
| Method | Endpoint | Description |
|---------|------------------|-----------------------------|
| **GET** | `/books` | Get all books |
| **GET** | `/books/author/{author_name}` | Get books by author (path parameter) |
| **GET** | `/books/author/?author_name=Author One` | Get books by author (query parameter) |
| **GET** | `/books/{title_name}/?category=Science` | Get books by title and category |
| **POST** | `/books/create_book` | Add a new book (pass JSON body) |
| **PUT** | `/books/update_book` | Update an existing book |
| **DELETE** | `/books/delete/delete_book/{book_title}` | Delete a book by title |

## Example JSON Payloads 📌  
### **POST - Create a Book**  
```json
{
  "title": "New Book",
  "author": "New Author",
  "category": "Fiction"
}
```
### **PUT - Update a Book**  
```json
{
  "title": "Title One",
  "author": "Updated Author",
  "category": "Updated Category"
}
```

