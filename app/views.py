from app import app

from flask import render_template


@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/Home.html")
def Home():
     return render_template("Home.html")
