📚 Bookstore API 2


A simple FastAPI-based project that allows users to manage a collection of books. It supports full CRUD operations: creating, reading, updating, and deleting books — with additional filtering by rating and publish year.


Features 🚀
✅ Get all books
✅ Get a book by ID
✅ Get books by rating
✅ Get books by published date
✅ Create a new book
✅ Update an existing book
✅ Delete a book


Run the API ▶️

API will be accessible at:
🔗 http://127.0.0.1:8000
📘 Swagger docs: http://127.0.0.1:8000/docs

API Endpoints 🔗
Method	Endpoint	Description
GET	/books	Get all books
GET	/book/{book_id}	Get a book by ID
GET	/book/?book_rating=5	Get books filtered by rating (1–5)
GET	/book/publish/?publish_date=2024	Get books filtered by published year
POST	/create-books	Add a new book (JSON body required)
PUT	/book/update_book	Update an existing book
DELETE	/book/{book_id}	Delete a book by ID

Example JSON Payloads 📌
POST - Create a Book
json
Copy
Edit
{
  "title": "A New Book",
  "author": "Author Name",
  "description": "Short description of the book",
  "rating": 5,
  "published_date": 2024
}
PUT - Update a Book
json
Copy
Edit
{
  "id": 1,
  "title": "Updated Title",
  "author": "Updated Author",
  "description": "Updated description",
  "rating": 4,
  "published_date": 2023
}
Tech Stack 🛠
FastAPI

Pydantic

Uvicorn (ASGI server)
