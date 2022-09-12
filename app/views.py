from app import app

from flask import render_template


@app.route("/")
def index():
    return render_template("index2.html") 

@app.route("/index2.html")
def index2():
     return render_template("index2.html")

@app.route("/Operations2.html")
def Operations():
    return render_template("Operations2.html")


