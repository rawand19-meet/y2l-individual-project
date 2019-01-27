from flask import Flask, render_template, request, redirect, url_for
from database import *

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home_page.html")

@app.route('/female')
def female():
    return render_template("female.html")

@app.route('/female2')
def female2():
    return render_template("female2.html")


@app.route('/male')
def male():
    return render_template("male.html")


@app.route('/male2')
def male2():
    return render_template("male2.html")


@app.route('/profile', methods=['GET', 'POST'])
def profile():
 
  pass

# @app.route('/search', methods=['POST'])
# def search():
#     keyword = request.form["keyword"]

#     values = search_db(keyword)

#     item = values.first()

#     return render_template("item.html", item=item)



@app.route('/search', methods=["GET", "POST"])
def search_results():
  if request.method == "POST":
    keyword = request.form["keyword"]
    results = search_db(keyword) 
    item = results.first() if results else None
    return render_template("item.html", item=item)
  else:
    return render_template('female.html', query=query, results=results)





if __name__ == '__main__':
   app.run(debug = True)



# @app.route('/')
# def home_page():
#     return render_template("female.html")

# @app.route('/')
# def home_page():
#     return render_template("home_page.html")
    

    





