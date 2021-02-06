import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("base.html")


@app.route("/games")
def games():
    return render_template("games_template.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if user already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exisits")
            return redirect(url_for("register"))

        # Check if passwords match
        password = request.form.get("password")
        confirm_password = request.form.get("confirmPassword")

        if password == confirm_password:
            # Add new user to db
            register = {
                "username": request.form.get("username").lower(),
                "email": request.form.get("email").lower(),
                "password": generate_password_hash(password)
            }
            mongo.db.users.insert_one(register)

            # Add user into session cookie
            session["user"] = request.form.get("username").lower()
            flash("Registration Successful")
            return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if username exists in the db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Check if hashed password matches user input
            if check_password_hash(
               existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome {}".format(
                    request.form.get("username").capitalize()))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # Invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>")
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)


@app.route("/logout")
def logout():
    # Remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
