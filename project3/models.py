from fastapi import FastAPI, UploadFile, File, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from sentence_transformers import SentenceTransformer

from database import SessionLocal, engine
from models import Base, DocumentChunk
from schemas import QueryRequest, QueryResponse
from utils import chunk_text, cosine_similarity

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Load embedding model once at startup
model = SentenceTransformer("all-MiniLM-L6-v2")


# ==========================
# DB Dependency
# ==========================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


# ==========================
# Upload Endpoint
# ==========================
@app.post("/upload/")
async def upload_document(
    file: UploadFile = File(...),
    db: db_dependency = None
):
    content = (await file.read()).decode("utf-8")

    chunks = chunk_text(content)

    for chunk in chunks:
        embedding = model.encode(chunk).tolist()

        db_chunk = DocumentChunk(
            content=chunk,
            embedding=embedding
        )

        db.add(db_chunk)

    db.commit()

    return {
        "message": f"Stored {len(chunks)} chunks successfully"
    }


# ==========================
# Query Endpoint
# ==========================
@app.post("/query/", response_model=QueryResponse)
def query_documents(
    request: QueryRequest,
    db: db_dependency = None
):
    query_embedding = model.encode(request.query).tolist()

    documents = db.query(DocumentChunk).all()

    similarities = []

    for doc in documents:
        score = cosine_similarity(query_embedding, doc.embedding)
        similarities.append((score, doc.content))

    # Sort by highest similarity
    top_chunks = sorted(
        similarities,
        key=lambda x: x[0],
        reverse=True
    )[:5]

    results = [
        {"content": content, "score": float(score)}
        for score, content in top_chunks
    ]

    return {"results": results}


from database import Base
from sqlalchemy import Column, Integer, String, Boolean,ForeignKey


class Users(Base):
    __tablename__ = 'users'
    
    id = Column(Integer,primary_key=True,index=True)
    email = Column(String,unique=True)
    username = Column(String,unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean,default=True)
    role = Column(String)
    phone_number = Column(String)

class Todos(Base):
    __tablename__ = 'todos'
    
    id = Column(Integer,primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean,default=False)
    owner_id = Column(Integer,ForeignKey("users.id"))
    
