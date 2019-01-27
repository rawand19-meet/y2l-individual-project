from flask import Flask, render_template,session, request, redirect, url_for


app = Flask(__name__)

@app.route('/')
def home():
  if session.get('display_login') == True:
    session['display_login'] = False
    return render_template('home_page.html', logged_in=True)
  else:
    return render_template('home_page.html', logged_in=False)


# @app.route('/')
# def home_page():
#     return render_template('home_page.html')




@app.route('/signup', methods=['GET', 'POST'])
def signup_route():
  if request.method == 'GET':
    return render_template('signup.html')
  else:
    print ('Received POST request for sign up!')
    # nationality = request.form['nationality']
    name = request.form['name']
    username=request.form['username']
    password= request.form['password']
    
    g=add_user(name,username, password)

    if g!=None:
      print ('we already have a user with that name')
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login_route():
  if 'logged_in' in session and session['logged_in']==True:
    return redirect (url_for('home'))
  if request.method == 'POST':
    # return redirect (url_for('home'))
    print('hey')
    username = request.form['username']
    user=query_by_username(username)
    if user==None:
      return redirect (url_for('signup_route'))
    else:
      # if request.form.get('password') and
        if request.form['password']== user.password:
            session["logged_in"] = True
            session["user_id"] = user.name
            session["display_login"] = True


        return render_template('home_page.html')
  else:
    return render_template('login.html') 

# @app.route('/signup')
# def signup():
#     return render_template('signup.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')

@app.route('/logout')
def logout_route():
  if 'user_id' in session:
    del session['user_id']
    session['logged_in']=False
  return redirect(url_for('home'))
  print('logged out')



@app.route('/')
def home_page():
    return render_template("home_page.html")


@app.route('/')
def homepage1():
    return render_template("homepage1.html")


@app.route('/')
def login():
    return render_template("login.html")

@app.route('/')
def signup():
    return render_template("signup.html")

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
    






