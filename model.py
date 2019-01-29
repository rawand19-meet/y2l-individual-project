from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine


Base=declarative_base()


class Products(Base):

  __tablename__ = 'Product'
  id = Column(Integer, primary_key=True)
  name = Column(String)
  picture = Column(String)
  category =Column(String)
