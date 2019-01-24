from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///looks.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_products(name, picture, category):
	add_products= Products(
        name=name,
        picture=picture,
        category=category)
	session.add(add_products)
	session.commit()


def search_db(keyword):
	single_search = session.query(Products).filter(Products.picture==keyword or Products.category==keyword)
	if single_search.first():
		return single_search
	else:
		return None
# add_products("john Masters Organics","h1.jpg ","woman" )
# add_products("Purechimp","h2.jpg ","woman" )
# add_products("Odylique by Essential Care","h3.jpg ","woman" )
# add_products("john Masters Organics","h4.jpg ","woman" )
# add_products("Rahua","h5.jpg ","woman" )
# add_products("Madara","h66.jpg ","woman")
# add_products("Ogario London","h7.jpg ","woman" )
# add_products("Essentially Nature","h8.jpg ","woman" )
# add_products("PHB Ethical Beauty","h9.jpg ","woman" )






# add_products("Kimberly Sayer","s1.jpg ","woman" )
# add_products("lyonsleaf","s2.jpg ","woman" )
# add_products("Dr.Hauschka","s3.jpg ","woman" )
# add_products("Balm Balm","s4.jpg ","woman" )
# add_products("Balm Balm","s5.jpg ","woman" )
# add_products("Pacifica","s6.jpg ","woman")
# add_products("Antipodes","s7.jpg ","woman" )
# add_products("Antipodes","s8.jpg ","woman" )
# add_products("Laidbare","s9.jpg ","woman" )


   
def query_all():
	products=session.query(Products).all()
	return products

def query_by_name(name):
	products=session.query(Products).filter_by(name=name).first()
	return products 


def query_by_category(category):
	products=session.query(Products).filter_by(category=category).first()
	return products


print(query_all())