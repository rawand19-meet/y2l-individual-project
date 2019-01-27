from model import *
from model import Base, User   
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///looks.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(name,username, password):
    print("Added a user!")
    user = User(name=name,username=username ,password=password)
    session.add(user)
    session.commit()

def get_all_users():
  users = session.query(User).all()
  return users


def query_by_name(name):
  user= session.query(User).filter_by(name=name).first()
  return user 

def query_by_username(username):
  user= session.query(User).filter_by(username=username).first()
  print 'user: ' + str(user)
  return user 

def query_by_password(password):
  users= session.query(User).filter_by(password=password).all()
  return user



def add_products(name, picture, category):
	add_products= Products(
        name=name,
        picture=picture,
        category=category)
	session.add(add_products)
	session.commit()


def search_db(keyword):
	single_search = session.query(Products).filter(Products.picture==keyword or Products.category==keyword or Products.name==keyword)
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


# add_products("Rahua","m1.jpg ","man" )
# add_products("Rahua","m2.jpg ","man" )
# add_products("Madara","m3.jpg ","man" )
# add_products("GK Natural Creations","m4.jpg ","man" )
# add_products("Kae","m5.jpg ","man" )
# add_products("Lyonsleaf","m6.jpg ","man" )
# add_products("Ogario London","m7.jpg ","man" )
# add_products("TABITHA JAMES KRAAN","m8.jpg ","man" )
# add_products("Pure potions","m9.jpg ","man" )

# add_products("Trilogy","t1.jpg ","man" )
# add_products("Balm Balm","t2.jpg ","man" )
# add_products("Antipodes","t3.jpg ","man" )
# add_products("REN","t4.jpg ","man" )
# add_products("Sukin","t5.jpg ","man" )
# add_products("Planted","t6.jpg ","man" )
# add_products("Laidbare","t7.jpg ","man" )
# add_products("PHB Ethical Beauty ","t8.jpg ","man" )
# add_products("1001 remedies","t9.jpg ","man" )


   
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
