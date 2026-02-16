from pydantic import BaseModel
from typing import List

class QueryRequest(BaseModel):
    query: str

class ChunkResult(BaseModel):
    content: str
    score: float

class QueryResponse(BaseModel):
    results: List[ChunkResult]



from sqlalchemy import Column, Integer, Text, JSON
from database import Base

class DocumentChunk(Base):
    __tablename__ = "document_chunks"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    embedding = Column(JSON, nullable=False)


from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("document-search")

@mcp.tool()
def ask_document(question: str) -> str:
    try:
        response = requests.post(
            "http://127.0.0.1:8000/query/",
            json={"query": question},
            timeout=10
        )

        if response.status_code != 200:
            return f"FastAPI error: {response.status_code} {response.text}"

        data = response.json()
        results = data.get("results", [])

        if not results:
            return "No relevant results found."

        combined_context = "\n\n".join(
            f"(score={round(r['score'],3)})\n{r['content']}"
            for r in results
        )

        return combined_context

    except Exception as e:
        return f"MCP tool error: {str(e)}"


if __name__ == "__main__":
    mcp.run()


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./rag.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()



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
    
