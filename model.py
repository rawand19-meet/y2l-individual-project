from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_whooshalchemy import whoosh_index
from app import app

db = SQLAlchemy()

class User(db.model):
  __searchable__ = ['name']
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64))

whoosh_index(app, User)
Base = declarative_base()

# Write your classes here :
class Product(Base):
    pass