from sqlalchemy import Column, Integer, String, select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from Common.Share.BaseModel import BaseModel
# 声明基类
Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'users'
    uid = Column(Integer, primary_key=True, index=True)
    account = Column(String(64), unique=True, index=True)
    password = Column(String(32), unique=False, index=True)
    inner = Column(Integer, unique=False, index=True)
    role = Column(String(32), unique=False, index=True)
    power = Column(String(32), unique=False, index=True)
    member_id = Column(String(64), unique=False, index=True)