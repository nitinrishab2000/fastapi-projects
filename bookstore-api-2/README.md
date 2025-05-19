# 📚 Bookstore API 2

A simple **FastAPI** project to manage a collection of books. It supports full CRUD operations and lets you filter books by rating and published year.

---

## 🚀 Features

- ✅ Get all books  
- ✅ Get book by ID  
- ✅ Get books by rating  
- ✅ Get books by publish year  
- ✅ Create a new book  
- ✅ Update a book  
- ✅ Delete a book  

---

## ▶️ How to Run the API

### 🔧 Step 1: Install dependencies

Create and activate a virtual environment (optional but recommended):

```bash
python -m venv fastapienv
source fastapienv/bin/activate  # On Windows: fastapienv\Scripts\activate
```

Install FastAPI and Uvicorn:

```bash
pip install fastapi uvicorn
```

### ▶️ Step 2: Run the API server

Assuming your file is named `main.py` and contains the FastAPI app as `app`, run:

```bash
uvicorn main:app --reload
```

Server will start at:

- Swagger Docs: http://127.0.0.1:8000/docs  
- ReDoc Docs: http://127.0.0.1:8000/redoc  

---

## 📌 API Endpoints

| Method | Endpoint                                 | Description                                  |
|--------|------------------------------------------|----------------------------------------------|
| GET    | `/books`                                 | Get all books                                |
| GET    | `/book/{book_id}`                        | Get a single book by ID                      |
| GET    | `/book/?book_rating=5`                   | Get books with specific rating (1 to 5)      |
| GET    | `/book/publish/?publish_date=2024`       | Get books by published year (2000 to 2030)   |
| POST   | `/create-books`                          | Create a new book (send JSON body)           |
| PUT    | `/book/update_book`                      | Update an existing book by ID (send JSON)    |
| DELETE | `/book/{book_id}`                        | Delete a book by its ID                      |

---

## 📘 Example Request Payloads

### 🆕 POST `/create-books`

```json
{
  "title": "New Book Title",
  "author": "Author Name",
  "description": "A brief description.",
  "rating": 5,
  "published_date": 2025
}
```

### ✏️ PUT `/book/update_book`

```json
{
  "id": 1,
  "title": "Updated Book Title",
  "author": "Updated Author",
  "description": "Updated description here.",
  "rating": 4,
  "published_date": 2023
}
```

