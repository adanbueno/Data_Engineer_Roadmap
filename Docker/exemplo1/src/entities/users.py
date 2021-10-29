from sqlalchemy import Column, Integer, String
from src.config import Base

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    
    def __repr__(self) -> str:
        return f"Users [name={self.name}]"
        