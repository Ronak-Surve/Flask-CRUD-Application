from flask import Flask, render_template, request, redirect, url_for, session
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "user123"
app.permanent_session_lifetime = timedelta(minutes=1)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return "<h1> Home Page </h1>"

@app.route("/user")
def welcome():
    if "user" in session:
        user = session["user"]
        return f"Hello {user}"
    else :
        return redirect(url_for("login"))
    
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        username = request.form["name"]
        session["user"] = username
        return redirect(url_for("welcome"))
    else:
        if "user" in session:
            return redirect(url_for("welcome"))
        return render_template("login.html")
    

@app.route("/logout")
def logout():
    session.pop("user")
    return redirect(url_for("login"))
    
if __name__ in "__main__":
    app.run(debug=True)