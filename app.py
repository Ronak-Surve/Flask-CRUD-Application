from flask import Flask, render_template, request, redirect, url_for
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return "<h1> Home Page </h1>"

@app.route("/<name>")
def welcome(name):
    return f"Hello {name}"

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["name"]
        return redirect(url_for("welcome", name=username))
    else:
        return render_template("login.html")
    
if __name__ in "__main__":
    app.run(debug=True)