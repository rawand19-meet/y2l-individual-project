from models import *
from wtforms import StringField
from wtforms.validators import DataRequired
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///natural looks.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def function(parameter):
    pass

class SearchForm(Form):
  search = StringField('search', [DataRequired()])
  submit = SubmitField('Search',
                       render_kw={'class': 'btn btn-success btn-block'})

