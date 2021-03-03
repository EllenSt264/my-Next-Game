import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo, pymongo
from flask_paginate import Pagination, get_page_args
from bson.objectid import ObjectId
from bson.json_util import dumps
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
    per_page = 9
    offset = ((page - 1) * per_page)

    total = bestsellers.count()
    pagination_bestsellers = bestsellers[offset: offset + per_page]

    pagination = Pagination(
        page=page, per_page=per_page, total=total,
        css_framework='materialize')

    return render_template(
        "base.html", bestsellers=pagination_bestsellers,
        pagination=pagination, awardwinners=awardwinners
    )


# ===================
# Game pages template
# ===================

@app.route("/games")
def games():
    return render_template("games-template.html")


# ===================
# Search
# ===================

@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")

    mongo.db.pc_games.create_index([("game_title", 1)])
    games = mongo.db.pc_games.find(
        {"$text": {"$search": query}})

    return render_template("games-search_results.html", games=games)


# ===================
# PC Games
# ===================

@app.route("/pc-games")
def pc_games():
    pc_games = mongo.db.pc_games.find()

    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    per_page = 8
    offset = ((page - 1) * per_page)

    total = pc_games.count()
    pagination_pc_games = pc_games[offset: offset + per_page]

    pagination = Pagination(
        page=page, per_page=per_page, total=total,
        css_framework='materialize')

    return render_template(
        "games-pc.html", pc_games=pagination_pc_games,
        pagination=pagination)


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
        "games-action.html", action_games=pagination_action_games, 
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
        "games-adventure.html", adventure_games=pagination_adventure_games, 
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
        "games-rpg.html", RPG_games=pagination_RPG_games, 
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
        "games-strategy.html", strategy_games=pagination_strategy_games, 
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
        "games-multiplayer.html",
        multiplayer_games=pagination_multiplayer_games,
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
            return redirect(url_for("profile_games", username=session["user"]))

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
                    "profile_games", username=session["user"]))
            else:
                # Invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

    return render_template("login.html")


# ==========
# Profile
# ==========

@app.route("/profile")
def profile():
    return render_template("profile-template.html")


@app.route("/profile/<username>")
def profile_games(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    user_games = mongo.db.user_games.find()

    return render_template("profile-games_list.html", username=username,
                           user_games=user_games)


# ================
# User Games List
# ================

@app.route("/games/<username>")
def user_list(username):
    user_games = mongo.db.user_games.find()
    return render_template("games-user_list.html", username=session["user"],
                           user_games=user_games)


# ==========
# Reviews
# ==========

@app.route("/community-reviews")
def reviews():
    return render_template("games-reviews.html")


# ==========
# Reviews
# ==========

@app.route("/submit-review")
def submit_review():
    return render_template("games-review_form.html")


# ==============
# Export to JS
# ==============

def export_data():
    games = mongo.db.pc_games.find({})

    def writeToJS():
        file = open("static/js/data.js", "w")
        file.write('const gameData = [')
        for game in games:
            file.write(dumps(game["game_title"]))
            file.write(', ')
        file.write(']')

    writeToJS()


export_data()


# ==========
# Add game
# ==========

@app.route("/add_game/<game_id>")
def add_game(game_id):
    # Grab game data from database
    game = mongo.db.pc_games.find_one({"_id": ObjectId(game_id)})

    # Create empty lists to add dict data into
    title = []
    tags = []
    img_sm = []
    img_full = []
    platform = []
    link = []

    # Sift through dictionary data and add to lists
    for k, v in game.items():
        if k == "game_title":
            title.append(v)
            dict_game_title = v
        if k == "game_top_tags":
            tags.append(v)
        if k == "game_img_sm":
            img_sm.append(v)
        if k == "game_img_full":
            img_full.append(v)
        if k == "platform_tags_pc":
            platform.append(v)
        if k == "game_link":
            link.append(v)

    # Construct new dicitonary
    data = {
            "game_title": title[0],
            "game_img_sm": img_sm[0],
            "game_img_full": img_full[0],
            "game_tags": tags[0],
            "platform_pc": platform[0],
            "game_link": link[0],
            "username": session["user"],
            "stage": "next"
        }

    # Check if a user has already added a game with the same to the db
    existing_data = mongo.db.user_games.find_one(
        {"$and": [{"username": session["user"]},
                  {"game_title": dict_game_title}]})

    if existing_data is None:
        mongo.db.user_games.insert_one(data)
        flash("Game Successfully Added to List")

    elif existing_data:
        flash("You've Already Added This Game")

    else:
        mongo.db.user_games.insert_one(data)
        flash("Game Successfully Added to List")

    return redirect(url_for("pc_games", game_id=game_id))


# ====================
# Edit User Games List
# ====================

@app.route("/profile/<username>/edit-games")
def edit_user_games_list(username):
    return render_template(
        "profile-games_list_form.html", username=session["user"])


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
