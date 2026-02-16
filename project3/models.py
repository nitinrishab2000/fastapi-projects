import numpy as np

def chunk_text(text: str, chunk_size=1500, overlap=200):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks


def cosine_similarity(vec1, vec2):
    v1 = np.array(vec1)
    v2 = np.array(vec2)
    return float(
        np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    )


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
    
