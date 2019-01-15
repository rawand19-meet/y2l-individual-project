from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home_page.html")
@app.route('/female')
def female():
    return render_template("female.html")

@app.route('/male')
def male():
    return render_template("male.html")

@app.route('/backgroundcolor')
def backgroundcolor():
    return render_template("home_page.css")



if __name__ == '__main__':
   app.run(debug = True)



# @app.route('/')
# def home_page():
#     return render_template("female.html")

# @app.route('/')
# def home_page():
#     return render_template("home_page.html")
    

   	





