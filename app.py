from flask import Flask, render_template


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

@app.route('/')
def index():
  if current_user.is_authenticated:
    return redirect(url_for('profile'))
  return render_template('index.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
  # some code to display user profile page
  pass

@app.route('/search', methods=['POST'])
def search():
  form = SearchForm()
  if not form.validate_on_submit():
    return redirect(url_for('index'))
  return redirect((url_for('search_results', query=form.search.data)))

@app.route('/search_results/<query>')
def search_results(query):
  results = User.query.whoosh_search(query).all()
  return render_template('female.html', query=query, results=results)



if __name__ == '__main__':
   app.run(debug = True)



# @app.route('/')
# def home_page():
#     return render_template("female.html")

# @app.route('/')
# def home_page():
#     return render_template("home_page.html")
    

    





