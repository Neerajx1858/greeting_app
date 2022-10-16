from flask import Flask, render_template, request, flash

app = Flask(__name__) #to create a class for our app
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key' # to set the secret key unique otherwise it will cause server internal error

#to select a route for app
@app.route("/hello") #this basically represent the last part of our url
def index():
    flash("What's your name?")#to set an initial message
    return render_template("index.html") #to display the html with flask

#to create a new route to display a difffrent message when we press the submit button
@app.route("/greet", methods=["POST","GET"])
def greet():
    flash("Hi "+str(request.form['name_input']) + ", great to see ya :)")
    request.form['name_input']
    return render_template("index.html")