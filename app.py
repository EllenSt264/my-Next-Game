import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo, pymongo
from flask_paginate import Pagination, get_page_args
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# ==========
# Homepage
# ==========

@app.route("/")
@app.route("/home")
def home():

    # The following code is based of this source:
    # "https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9"

    # Grab bestsellers from db
    bestsellers = mongo.db.steam_bestsellers.find().sort(
        "game_index", pymongo.ASCENDING)

    # Grab award winners from db
    awardwinners = mongo.db.steam_awardwinners.find().sort(
        "game_index", pymongo.ASCENDING)

    # Initalize pagination
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    per_page = 8
    offset = ((page - 1) * per_page)

    # Bestsellers
    total_bestsellers = bestsellers.count()
    pagination_bestsellers = bestsellers[offset: offset + per_page]

    pagination_for_bestsellers = Pagination(
        page=page, per_page=per_page, total=total_bestsellers, 
        css_framework='materialize')

    # Award winners
    total_awards = awardwinners.count()
    pagination_awardwinners = awardwinners[offset: offset + per_page]

    pagination_for_awardwinners = Pagination(
        page=page, per_page=per_page, total=total_awards,
        css_framework='materialize')

    return render_template(
        "base.html", bestsellers=pagination_bestsellers,
        awardwinners=pagination_awardwinners,
        pagination_bs=pagination_for_bestsellers, 
        pagination_aw=pagination_for_awardwinners)


# ===================
# Game pages template
# ===================

@app.route("/games")
def games():
    return render_template("games_template.html")


# ===================
# PC Games
# ===================

@app.route("/pc-games")
def pc_games():
    return render_template("pc-games.html")


# ===================
# Action Games
# ===================

@app.route("/action-games")
def action_games():

    action_games = mongo.db.steam_action_games.find()

    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    per_page = 8
    offset = ((page - 1) * per_page)

    total = action_games.count()
    pagination_action_games = action_games[offset: offset + per_page]

    pagination = Pagination(
        page=page, per_page=per_page, total=total,
        css_framework='materialize')

    return render_template(
        "action_games.html", action_games=pagination_action_games, 
        pagination=pagination)


# ===================
# Adventure Games
# ===================

@app.route("/adventure-games")
def adventure_games():
    adventure_games = mongo.db.steam_adventure_games.find()

    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    per_page = 8
    offset = ((page - 1) * per_page)

    total = adventure_games.count()
    pagination_adventure_games = adventure_games[offset: offset + per_page]

    pagination = Pagination(
        page=page, per_page=per_page, total=total,
        css_framework='materialize')

    return render_template(
        "adventure_games.html", adventure_games=pagination_adventure_games, 
        pagination=pagination)


# ===================
# RPG Games
# ===================

@app.route("/RPG-games")
def RPG_games():
    RPG_games = mongo.db.steam_RPG_games.find()

    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    per_page = 8
    offset = ((page - 1) * per_page)

    total = RPG_games.count()
    pagination_RPG_games = RPG_games[offset: offset + per_page]

    pagination = Pagination(
        page=page, per_page=per_page, total=total,
        css_framework='materialize')

    return render_template(
        "RPG_games.html", RPG_games=pagination_RPG_games, 
        pagination=pagination)


# ===================
# Strategy Games
# ===================

@app.route("/strategy-games")
def strategy_games():
    strategy_games = mongo.db.steam_strategy_games.find()

    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    per_page = 8
    offset = ((page - 1) * per_page)

    total = strategy_games.count()
    pagination_strategy_games = strategy_games[offset: offset + per_page]

    pagination = Pagination(
        page=page, per_page=per_page, total=total,
        css_framework='materialize')

    return render_template(
        "strategy_games.html", strategy_games=pagination_strategy_games, 
        pagination=pagination)


# ===================
# Multiplayer Games
# ===================

@app.route("/multiplayer-games")
def multiplayer_games():
    multiplayer_games = mongo.db.steam_multiplayer_games.find()

    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    per_page = 8
    offset = ((page - 1) * per_page)

    total = multiplayer_games.count()
    pagination_multiplayer_games = multiplayer_games[offset: offset + per_page]

    pagination = Pagination(
        page=page, per_page=per_page, total=total,
        css_framework='materialize')

    return render_template(
        "multiplayer_games.html", multiplayer_games=pagination_multiplayer_games, 
        pagination=pagination)


# ==========
# Register
# ==========

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


# ==========
# Login
# ==========

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


# ==========
# Profile
# ==========

@app.route("/profile/<username>")
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)


# ==========
# Logout
# ==========

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
