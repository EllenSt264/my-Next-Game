"""
    ** Attribution:

    * Adding Pagination:
    "https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9"#

    * Finding all the values of a specific key within a collection:
    "https://stackoverflow.com/questions/34861949/how-to-find-all-values-for-a-specific-key-in-pymongo"

    * Redirecting users back to the same page:
    "https://stackoverflow.com/questions/41270855/flask-redirect-to-same-page-after-form-submission/41272173"

    * Returning a random document from MongoDB collection:
    "https://stackoverflow.com/questions/2824157/random-record-from-mongodb"

    * Selecting a random item from a list:
    "https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list"

    * Exporting MongoDB collection to local JSON/JS file:
    "https://stackoverflow.com/questions/60584148/export-pymongo-collection-to-a-json-file"

    * Returning documents from MongoDB without duplicates:
    "https://stackoverflow.com/questions/11470614/mongodb-return-all-documents-by-field-without-duplicates"

"""

import os
import datetime
import random
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
    # Grab bestsellers from db
    bestsellers = mongo.db.all_pc_games.find({"bestseller": True})

    # Grab award winners from db
    awardwinners = mongo.db.all_pc_games.find({"awardwinner": True})

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
        pagination=pagination, awardwinners=awardwinners)


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

    mongo.db.all_pc_games.create_index([("game_title", "text")])
    games = mongo.db.all_pc_games.find(
        {"$text": {"$search": query}})

    # Pagination
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    per_page = 9
    offset = ((page - 1) * per_page)

    total = games.count()
    pagination_games = games[offset: offset + per_page]

    pagination = Pagination(
        page=page, per_page=per_page, total=total,
        css_framework='materialize')

    return render_template(
        "games-search_results.html", games=pagination_games,
        pagination=pagination)


@app.route("/community-reviews/search", methods=["GET", "POST"])
def search_reviews():
    query = request.form.get("review-query")

    mongo.db.user_reviews.create_index([("game_title", "text")])
    reviews = mongo.db.user_reviews.find(
        {"$text": {"$search": query}})

    # Pagination
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    per_page = 9
    offset = ((page - 1) * per_page)

    total = reviews.count()
    pagination_game_reviews = reviews[offset: offset + per_page]

    pagination = Pagination(
        page=page, per_page=per_page, total=total,
        css_framework='materialize')

    return render_template(
        "games-reviews.html", game_reviews=pagination_game_reviews,
        pagination=pagination)


# ===================
# PC Games
# ===================

@app.route("/pc-games", methods=["GET", "POST"])
def pc_games():
    pc_games = mongo.db.all_pc_games.find()

    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    per_page = 6
    offset = ((page - 1) * per_page)

    total = pc_games.count()
    pagination_pc_games = pc_games[offset: offset + per_page]

    pagination = Pagination(
        page=page, per_page=per_page, total=total,
        css_framework='materialize')

    # Find site favourites
    favourites = mongo.db.site_favourites.distinct("game_title")

    # Sort filter

    if request.method == "POST":
        session["navSelect1"] = request.form.get("navSelect1").lower()
        session["navSelect2"] = request.form.get("navSelect2").lower()

    navSelect1 = session["navSelect1"]
    navSelect2 = session["navSelect2"]

    # Sort by Likes

    if navSelect1 == "likes" and navSelect2 == "desc":
        pagination_pc_games.sort("likes", pymongo.DESCENDING)

    elif navSelect1 == "likes" and navSelect2 == "asc":
        pagination_pc_games.sort("likes", pymongo.ASCENDING)

    # Sort by game title
    elif navSelect1 == "title" and navSelect2 == "desc":
        pagination_pc_games.sort("game_title", pymongo.DESCENDING)

    elif navSelect1 == "title" and navSelect2 == "asc":
        pagination_pc_games.sort("game_title", pymongo.ASCENDING)

    # Sort by bestseller
    elif navSelect1 == "bestseller" and navSelect2 == "desc":
        pagination_pc_games.sort("bestseller", pymongo.DESCENDING)

    elif navSelect1 == "bestseller" and navSelect2 == "asc":
        pagination_pc_games.sort("bestseller", pymongo.ASCENDING)

    # Sort by awardwinner
    elif navSelect1 == "awardwinner" and navSelect2 == "desc":
        pagination_pc_games.sort("awardwinner", pymongo.DESCENDING)

    elif navSelect1 == "awardwinner" and navSelect2 == "asc":
        pagination_pc_games.sort("awardwinner", pymongo.ASCENDING)

    # Sort by favourite
    elif navSelect1 == "favourite" and navSelect2 == "desc":
        pagination_pc_games.sort("favourite", pymongo.DESCENDING)

    elif navSelect1 == "favourite" and navSelect2 == "asc":
        pagination_pc_games.sort("favourite", pymongo.ASCENDING)

    return render_template(
        "games-pc.html", pc_games=pagination_pc_games,
        pagination=pagination, favourites=favourites,
        navSelect1=navSelect1, navSelect2=navSelect2)


# ===================
# Action Games
# ===================

@app.route("/action-games", methods=["GET", "POST"])
def action_games():
    pc_games = mongo.db.all_pc_games.find(
        {
            "$or": [
                {"action": True},
                {"game_top_tags": "Action"}
            ]
        }
    )

    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    per_page = 6
    offset = ((page - 1) * per_page)

    total = pc_games.count()
    pagination_pc_games = pc_games[offset: offset + per_page]

    pagination = Pagination(
        page=page, per_page=per_page, total=total,
        css_framework='materialize')

    # Find site favourites
    favourites = mongo.db.site_favourites.distinct("game_title")

    # Sort filter

    if request.method == "POST":
        session["navSelect1"] = request.form.get("navSelect1").lower()
        session["navSelect2"] = request.form.get("navSelect2").lower()

    navSelect1 = session["navSelect1"]
    navSelect2 = session["navSelect2"]

    # Sort by Likes

    if navSelect1 == "likes" and navSelect2 == "desc":
        pagination_pc_games.sort("likes", pymongo.DESCENDING)

    elif navSelect1 == "likes" and navSelect2 == "asc":
        pagination_pc_games.sort("likes", pymongo.ASCENDING)

    # Sort by game title
    elif navSelect1 == "title" and navSelect2 == "desc":
        pagination_pc_games.sort("game_title", pymongo.DESCENDING)

    elif navSelect1 == "title" and navSelect2 == "asc":
        pagination_pc_games.sort("game_title", pymongo.ASCENDING)

    # Sort by bestseller
    elif navSelect1 == "bestseller" and navSelect2 == "desc":
        pagination_pc_games.sort("bestseller", pymongo.DESCENDING)

    elif navSelect1 == "bestseller" and navSelect2 == "asc":
        pagination_pc_games.sort("bestseller", pymongo.ASCENDING)

    # Sort by awardwinner
    elif navSelect1 == "awardwinner" and navSelect2 == "desc":
        pagination_pc_games.sort("awardwinner", pymongo.DESCENDING)

    elif navSelect1 == "awardwinner" and navSelect2 == "asc":
        pagination_pc_games.sort("awardwinner", pymongo.ASCENDING)

    # Sort by favourite
    elif navSelect1 == "favourite" and navSelect2 == "desc":
        pagination_pc_games.sort("favourite", pymongo.DESCENDING)

    elif navSelect1 == "favourite" and navSelect2 == "asc":
        pagination_pc_games.sort("favourite", pymongo.ASCENDING)

    return render_template(
        "games-action.html", pc_games=pagination_pc_games,
        pagination=pagination, favourites=favourites,
        navSelect1=navSelect1, navSelect2=navSelect2)


# ===================
# Adventure Games
# ===================

@app.route("/adventure-games", methods=["GET", "POST"])
def adventure_games():
    pc_games = mongo.db.all_pc_games.find(
        {
            "$or": [
                {"category": "adventure"},
                {"game_top_tags": "Adventure"}
            ]
        }
    )

    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    per_page = 6
    offset = ((page - 1) * per_page)

    total = pc_games.count()
    pagination_pc_games = pc_games[offset: offset + per_page]

    pagination = Pagination(
        page=page, per_page=per_page, total=total,
        css_framework='materialize')

    # Find site favourites
    favourites = mongo.db.site_favourites.distinct("game_title")

    # Sort filter

    if request.method == "POST":
        session["navSelect1"] = request.form.get("navSelect1").lower()
        session["navSelect2"] = request.form.get("navSelect2").lower()

    navSelect1 = session["navSelect1"]
    navSelect2 = session["navSelect2"]

    # Sort by Likes

    if navSelect1 == "likes" and navSelect2 == "desc":
        pagination_pc_games.sort("likes", pymongo.DESCENDING)

    elif navSelect1 == "likes" and navSelect2 == "asc":
        pagination_pc_games.sort("likes", pymongo.ASCENDING)

    # Sort by game title
    elif navSelect1 == "title" and navSelect2 == "desc":
        pagination_pc_games.sort("game_title", pymongo.DESCENDING)

    elif navSelect1 == "title" and navSelect2 == "asc":
        pagination_pc_games.sort("game_title", pymongo.ASCENDING)

    # Sort by bestseller
    elif navSelect1 == "bestseller" and navSelect2 == "desc":
        pagination_pc_games.sort("bestseller", pymongo.DESCENDING)

    elif navSelect1 == "bestseller" and navSelect2 == "asc":
        pagination_pc_games.sort("bestseller", pymongo.ASCENDING)

    # Sort by awardwinner
    elif navSelect1 == "awardwinner" and navSelect2 == "desc":
        pagination_pc_games.sort("awardwinner", pymongo.DESCENDING)

    elif navSelect1 == "awardwinner" and navSelect2 == "asc":
        pagination_pc_games.sort("awardwinner", pymongo.ASCENDING)

    # Sort by favourite
    elif navSelect1 == "favourite" and navSelect2 == "desc":
        pagination_pc_games.sort("favourite", pymongo.DESCENDING)

    elif navSelect1 == "favourite" and navSelect2 == "asc":
        pagination_pc_games.sort("favourite", pymongo.ASCENDING)

    return render_template(
        "games-adventure.html", pc_games=pagination_pc_games,
        pagination=pagination, favourites=favourites,
        navSelect1=navSelect1, navSelect2=navSelect2)


# ===================
# RPG Games
# ===================

@app.route("/RPG-games", methods=["GET", "POST"])
def RPG_games():
    pc_games = mongo.db.all_pc_games.find(
        {
            "$or": [
                {"RPG": True},
                {"game_top_tags": "RPG"}
            ]
        }
    )

    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    per_page = 6
    offset = ((page - 1) * per_page)

    total = pc_games.count()
    pagination_pc_games = pc_games[offset: offset + per_page]

    pagination = Pagination(
        page=page, per_page=per_page, total=total,
        css_framework='materialize')

    # Find site favourites
    favourites = mongo.db.site_favourites.distinct("game_title")

    # Sort filter

    if request.method == "POST":
        session["navSelect1"] = request.form.get("navSelect1").lower()
        session["navSelect2"] = request.form.get("navSelect2").lower()

    navSelect1 = session["navSelect1"]
    navSelect2 = session["navSelect2"]

    # Sort by Likes

    if navSelect1 == "likes" and navSelect2 == "desc":
        pagination_pc_games.sort("likes", pymongo.DESCENDING)

    elif navSelect1 == "likes" and navSelect2 == "asc":
        pagination_pc_games.sort("likes", pymongo.ASCENDING)

    # Sort by game title
    elif navSelect1 == "title" and navSelect2 == "desc":
        pagination_pc_games.sort("game_title", pymongo.DESCENDING)

    elif navSelect1 == "title" and navSelect2 == "asc":
        pagination_pc_games.sort("game_title", pymongo.ASCENDING)

    # Sort by bestseller
    elif navSelect1 == "bestseller" and navSelect2 == "desc":
        pagination_pc_games.sort("bestseller", pymongo.DESCENDING)

    elif navSelect1 == "bestseller" and navSelect2 == "asc":
        pagination_pc_games.sort("bestseller", pymongo.ASCENDING)

    # Sort by awardwinner
    elif navSelect1 == "awardwinner" and navSelect2 == "desc":
        pagination_pc_games.sort("awardwinner", pymongo.DESCENDING)

    elif navSelect1 == "awardwinner" and navSelect2 == "asc":
        pagination_pc_games.sort("awardwinner", pymongo.ASCENDING)

    # Sort by favourite
    elif navSelect1 == "favourite" and navSelect2 == "desc":
        pagination_pc_games.sort("favourite", pymongo.DESCENDING)

    elif navSelect1 == "favourite" and navSelect2 == "asc":
        pagination_pc_games.sort("favourite", pymongo.ASCENDING)

    return render_template(
        "games-rpg.html", pc_games=pagination_pc_games,
        pagination=pagination, favourites=favourites,
        navSelect1=navSelect1, navSelect2=navSelect2)


# ===================
# Strategy Games
# ===================

@app.route("/strategy-games", methods=["GET", "POST"])
def strategy_games():
    pc_games = mongo.db.all_pc_games.find(
        {
            "$or": [
                {"strategy": True},
                {"game_top_tags": "Strategy"}
            ]
        }
    )

    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    per_page = 6
    offset = ((page - 1) * per_page)

    total = pc_games.count()
    pagination_pc_games = pc_games[offset: offset + per_page]

    pagination = Pagination(
        page=page, per_page=per_page, total=total,
        css_framework='materialize')

    # Find site favourites
    favourites = mongo.db.site_favourites.distinct("game_title")

    # Sort filter

    if request.method == "POST":
        session["navSelect1"] = request.form.get("navSelect1").lower()
        session["navSelect2"] = request.form.get("navSelect2").lower()

    navSelect1 = session["navSelect1"]
    navSelect2 = session["navSelect2"]

    # Sort by Likes

    if navSelect1 == "likes" and navSelect2 == "desc":
        pagination_pc_games.sort("likes", pymongo.DESCENDING)

    elif navSelect1 == "likes" and navSelect2 == "asc":
        pagination_pc_games.sort("likes", pymongo.ASCENDING)

    # Sort by game title
    elif navSelect1 == "title" and navSelect2 == "desc":
        pagination_pc_games.sort("game_title", pymongo.DESCENDING)

    elif navSelect1 == "title" and navSelect2 == "asc":
        pagination_pc_games.sort("game_title", pymongo.ASCENDING)

    # Sort by bestseller
    elif navSelect1 == "bestseller" and navSelect2 == "desc":
        pagination_pc_games.sort("bestseller", pymongo.DESCENDING)

    elif navSelect1 == "bestseller" and navSelect2 == "asc":
        pagination_pc_games.sort("bestseller", pymongo.ASCENDING)

    # Sort by awardwinner
    elif navSelect1 == "awardwinner" and navSelect2 == "desc":
        pagination_pc_games.sort("awardwinner", pymongo.DESCENDING)

    elif navSelect1 == "awardwinner" and navSelect2 == "asc":
        pagination_pc_games.sort("awardwinner", pymongo.ASCENDING)

    # Sort by favourite
    elif navSelect1 == "favourite" and navSelect2 == "desc":
        pagination_pc_games.sort("favourite", pymongo.DESCENDING)

    elif navSelect1 == "favourite" and navSelect2 == "asc":
        pagination_pc_games.sort("favourite", pymongo.ASCENDING)

    return render_template(
        "games-strategy.html", pc_games=pagination_pc_games,
        pagination=pagination, favourites=favourites,
        navSelect1=navSelect1, navSelect2=navSelect2)


# ===================
# Multiplayer Games
# ===================

@app.route("/multiplayer-games", methods=["GET", "POST"])
def multiplayer_games():
    pc_games = mongo.db.all_pc_games.find(
        {
            "$or": [
                {"multiplayer": True},
                {"game_top_tags": "Multiplayer"}
            ]
        }
    )

    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    per_page = 6
    offset = ((page - 1) * per_page)

    total = pc_games.count()
    pagination_pc_games = pc_games[offset: offset + per_page]

    pagination = Pagination(
        page=page, per_page=per_page, total=total,
        css_framework='materialize')

    # Find site favourites
    favourites = mongo.db.site_favourites.distinct("game_title")

    # Sort filter

    if request.method == "POST":
        session["navSelect1"] = request.form.get("navSelect1").lower()
        session["navSelect2"] = request.form.get("navSelect2").lower()

    navSelect1 = session["navSelect1"]
    navSelect2 = session["navSelect2"]

    # Sort by Likes

    if navSelect1 == "likes" and navSelect2 == "desc":
        pagination_pc_games.sort("likes", pymongo.DESCENDING)

    elif navSelect1 == "likes" and navSelect2 == "asc":
        pagination_pc_games.sort("likes", pymongo.ASCENDING)

    # Sort by game title
    elif navSelect1 == "title" and navSelect2 == "desc":
        pagination_pc_games.sort("game_title", pymongo.DESCENDING)

    elif navSelect1 == "title" and navSelect2 == "asc":
        pagination_pc_games.sort("game_title", pymongo.ASCENDING)

    # Sort by bestseller
    elif navSelect1 == "bestseller" and navSelect2 == "desc":
        pagination_pc_games.sort("bestseller", pymongo.DESCENDING)

    elif navSelect1 == "bestseller" and navSelect2 == "asc":
        pagination_pc_games.sort("bestseller", pymongo.ASCENDING)

    # Sort by awardwinner
    elif navSelect1 == "awardwinner" and navSelect2 == "desc":
        pagination_pc_games.sort("awardwinner", pymongo.DESCENDING)

    elif navSelect1 == "awardwinner" and navSelect2 == "asc":
        pagination_pc_games.sort("awardwinner", pymongo.ASCENDING)

    # Sort by favourite
    elif navSelect1 == "favourite" and navSelect2 == "desc":
        pagination_pc_games.sort("favourite", pymongo.DESCENDING)

    elif navSelect1 == "favourite" and navSelect2 == "asc":
        pagination_pc_games.sort("favourite", pymongo.ASCENDING)

    return render_template(
        "games-multiplayer.html", pc_games=pagination_pc_games,
        pagination=pagination, favourites=favourites,
        navSelect1=navSelect1, navSelect2=navSelect2)


# =================
# Site's Favourites
# =================

@app.route("/our-favourites")
def favourites():
    # Favourites db
    favourites = mongo.db.all_pc_games.find({"favourite": True})

    # Random game

    random_game = mongo.db.all_pc_games.aggregate([
        {"$match": {"favourite": True}},
        {"$sample": {"size": 1}}
    ])

    screenshots = []
    rand_game_title = []
    rand_game_summary = []
    rand_game_id = ""

    for data in random_game:
        rand_game_title.append(data["game_title"])
        rand_game_summary.append(data["game_summary"])
        rand_game_id = data["_id"]

        for img in data["screenshots"]:
            screenshots.append(img)

    rand_game_imgs = random.sample(screenshots, 3)

    return render_template(
        "games-favourites.html", favourites=favourites,
        rand_game_title=rand_game_title, rand_game_imgs=rand_game_imgs,
        rand_game_summary=rand_game_summary, rand_game_id=rand_game_id)


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
            # Generate random avatar for the new user
            random_avatar = mongo.db.avatars.aggregate(
                [{"$sample": {"size": 1}}]
            )
            for i in list(random_avatar):
                img_path = i["img_path"]
                img_alt = i["img_alt"]

            # Add new user to db
            register = {
                "username": request.form.get("username").lower(),
                "email": request.form.get("email").lower(),
                "password": generate_password_hash(password),
                "avatar": img_path,
                "avatar_desc": img_alt,
                "display_name": None,
                "admin": False
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
                # Create session cookie for user
                session["user"] = request.form.get("username").lower()

                # Create session cookie for admin
                user = mongo.db.users.find_one({
                    "username": request.form.get("username").lower()})
                admin = user["admin"]

                if admin is True:
                    session["admin"] = True
                else:
                    session["admin"] = False

                # Success - redirect to profile
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
# Game Likes
# ==========

@app.route("/like/<game_id>")
def like(game_id):
    # Grab game data from database
    game = mongo.db.all_pc_games.find_one({"_id": ObjectId(game_id)})
    game_title = game["game_title"]

    # Find ids of other games with the same game title
    other_games = mongo.db.all_pc_games.find({"game_title": game_title})
    other_game_ids = []

    for game in other_games:
        other_game_ids.append(game["_id"])

    # Find username
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    # Check if a user has already liked the game
    already_liked = mongo.db.all_pc_games.find_one(
        {"$and": [{"game_title": game_title},
                  {"liked_by": session["user"]}]})

    # Find game likes total
    like_num = mongo.db.all_pc_games.find_one(
        {"_id": ObjectId(game_id)})["likes"]

    new_like_num = int(like_num) + 1

    # Increment game likes
    if already_liked:
        flash("Sorry, but you've already liked this game.")
        return redirect(request.referrer)
    else:
        like = {"$set": {
            "likes": new_like_num,
            "liked_by": username
        }}
        for games in other_game_ids:
            mongo.db.all_pc_games.update({"_id": games}, like)

        flash("Liked added!")
        return redirect(request.referrer)


# ==============
# Request A Game
# ==============

@app.route("/request-a-game")
def request_game():
    return render_template("games-request_form.html")


# ==========================
# Admin Controls - Add to DB
# ==========================

@app.route("/admin/add-to-db", methods=["GET", "POST"])
def admin_add_to_db():
    if request.method == "POST":
        user = mongo.db.users.find_one({"username": session["user"]})

        # Check if passwords match
        password = request.form.get("password")
        confirm_password = request.form.get("confirmPassword")

        if password == confirm_password:
            # Check password
            if check_password_hash(user["password"], password):

                # Check if game already exisits
                existing_link = mongo.db.admin_game_links.find_one(
                    {"link": request.form.get("game-link")})

                if existing_link:
                    flash("Game Already In Waiting List")
                    return redirect(url_for("admin_add_to_db"))

                # Otherwise add to db
                game = {
                    "link": request.form.get("game-link"),
                    "category": request.form.getlist("category")
                }
                mongo.db.admin_game_links.insert_one(game)
                flash("Succesfully Added Data")
                return redirect(url_for("admin_add_to_db"))
            else:
                flash("Details Invalid")
                return redirect(url_for("admin_add_to_db"))
        else:
            flash("Details Invalid")
            return redirect(url_for("admin_add_to_db"))

    return render_template("admin-add_game.html")


# =============================
# Add game to Profile Game List
# =============================

@app.route("/add_game/<game_id>")
def add_game(game_id):
    # Grab game data from database
    game = mongo.db.all_pc_games.find_one({"_id": ObjectId(game_id)})

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

    return redirect(request.referrer)


# ================
# Profile Template
# ================

@app.route("/profile")
def profile():
    user = mongo.db.users.find_one({"username": session["user"]})
    return render_template("profile-template.html", user=user)


# =====================
# Edit Profile Template
# =====================

@app.route("/edit-profile/<username>")
def edit_profile_template(username):
    return render_template(
        "profile-edit_template.html", username=session["user"])


# ================
# Edit Profile
# ================

@app.route("/edit-profile/<username>/general", methods=["GET", "POST"])
def edit_profile(username):
    user = mongo.db.users.find_one({"username": session["user"]})
    if request.method == "POST":
        user_id = user["_id"]

        # Check password
        if check_password_hash(user["password"], request.form.get("password")):
            # Update db
            update = {"$set": {
                "email": request.values.get("edit-email"),
                "display_name": request.values.get("edit-displayName"),
                "first_name": request.values.get("edit-fname"),
                "last_name": request.values.get("edit-lname")
            }}

            mongo.db.users.update({"_id": user_id}, update)
            flash("Profile Setting Successfully Updated")
            return redirect(url_for('profile_games', username=session["user"]))

        else:
            # Invalid password
            flash("Incorrect Password")
            return redirect(url_for('edit_profile', username=session["user"]))

    return render_template(
        "profile-edit_general.html", username=session["user"], user=user)


# =====================
# Edit Profile - Avatar
# =====================

@app.route("/edit-profile/<username>/avatar")
def edit_profile_avatar(username):
    user_data = mongo.db.users.find()
    avatars = mongo.db.avatars.find().sort("img_alt", 1)
    return render_template(
        "profile-edit_avatar.html", username=session["user"],
        user_data=user_data, avatars=avatars)


# ============================
# Edit Profile - Update Avatar
# ============================

@app.route("/update-avatar/<avatar_id>", methods=["GET", "POST"])
def update_avatar(avatar_id):
    if request.method == "POST":
        user_id = mongo.db.users.find_one({"username": session["user"]})["_id"]
        avatar = mongo.db.avatars.find({"_id": ObjectId(avatar_id)})

        for i in list(avatar):
            img_path = i["img_path"]
            img_alt = i["img_alt"]

        update = {"$set": {
            "avatar": img_path,
            "avatar_desc": img_alt
        }}

        mongo.db.users.update({"_id": user_id}, update)
        flash("Avatar Successfully Updated")

    return redirect(url_for("edit_profile_avatar", username=session["user"]))


# ====================
# Profile - Games List
# ====================


@app.route("/profile/<username>")
def profile_games(username):
    user = mongo.db.users.find_one({"username": session["user"]})

    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    # Separate games into categories
    games_playing = list(mongo.db.user_games.find({"stage": "playing"}))
    games_next = list(mongo.db.user_games.find({"stage": "next"}))
    games_completed = list(mongo.db.user_games.find({"stage": "completed"}))

    # Find game titles for user_reviews and user_games
    fetch = {"game_title": 1}
    user_games = mongo.db.user_games.find({"username": username}, fetch)
    user_reviews = mongo.db.user_reviews.find({"username": username}, fetch)

    profile_games = []
    review_games = []
    matches = []

    # Sort through data and add to empty arrays
    for i in list(user_games):
        profile_games.append(i["game_title"])

    for i in list(user_reviews):
        review_games.append(i["game_title"])

    # Find title matches
    for i in profile_games:
        for x in review_games:
            if i == x:
                matches.append(x)

    return render_template(
        "profile-games_list.html", user=user, username=username,
        games_playing=games_playing, games_next=games_next,
        games_completed=games_completed, matches=matches)


# =========================
# Profile - Move to Playing
# =========================

@app.route("/play-now/<game_id>", methods=["GET", "POST"])
def game_to_playing(game_id):
    if request.method == "POST":
        update = {"$set": {"stage": "playing"}}
        mongo.db.user_games.update({"_id": ObjectId(game_id)}, update)
        flash("Game Successfully Moved to Playing")

    game = mongo.db.user_games.find_one({"_id": str(ObjectId(game_id))})
    return redirect(url_for(
        "profile_games", username=session["user"], game=game))


# ============================
# Profile - Move to Play Later
# ============================

@app.route("/play-next/<game_id>", methods=["GET", "POST"])
def game_to_next(game_id):
    if request.method == "POST":
        update = {"$set": {"stage": "next"}}
        mongo.db.user_games.update({"_id": ObjectId(game_id)}, update)
        flash("Game Successfully Moved to Play Later")

    game = mongo.db.user_games.find_one({"_id": str(ObjectId(game_id))})
    return redirect(url_for(
        "profile_games", username=session["user"], game=game))


# ===========================
# Profile - Move to Completed
# ===========================

@app.route("/completed/<game_id>", methods=["GET", "POST"])
def game_to_completed(game_id):
    if request.method == "POST":
        update = {"$set": {"stage": "completed"}}
        mongo.db.user_games.update({"_id": ObjectId(game_id)}, update)
        flash("Game Successfully Moved to Completed")

    game = mongo.db.user_games.find_one({"_id": ObjectId(game_id)})
    return redirect(url_for(
        "profile_games", username=session["user"], game=game))


# ===============================
# Profile - Remove Game from List
# ===============================

@app.route("/remove-game/<game_id>")
def remove_game(game_id):
    mongo.db.user_games.remove({"_id": ObjectId(game_id)})
    flash("Game Successfully Removed from Your List")
    return redirect(url_for("profile_games", username=session["user"]))


# ==============
# Export to JS
# ==============

def export_data():
    games = mongo.db.all_pc_games.find({}).distinct("game_title")

    def writeToJS():
        file = open("static/js/data.js", "w")
        file.write('const gameData = [')
        for game in games:
            file.write(dumps(game))
            file.write(', ')
        file.write(']')

    writeToJS()


export_data()


# ==========
# Reviews
# ==========

@app.route("/community-reviews")
def reviews():
    game_reviews = mongo.db.user_reviews.find({})

    # Pagination
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    per_page = 9
    offset = ((page - 1) * per_page)

    total = game_reviews.count()
    pagination_game_reviews = game_reviews[offset: offset + per_page]

    pagination = Pagination(
        page=page, per_page=per_page, total=total,
        css_framework='materialize')

    return render_template(
        "games-reviews.html", game_reviews=pagination_game_reviews,
        pagination=pagination)


# ======================
# Profile - User Reviews
# ======================

@app.route("/profile/<username>/reviews")
def profile_reviews(username):
    reviews = mongo.db.user_reviews.find({})
    user = mongo.db.users.find_one({"username": session["user"]})
    return render_template(
        "profile-reviews.html", username=session["user"],
        reviews=reviews, user=user)


# =============
# Submit Review
# =============

@app.route("/submit-review", methods=["GET", "POST"])
def submit_review():
    if request.method == "POST":

        title = request.form.get("query")
        game = mongo.db.all_pc_games.find_one({"game_title": title})
        img_full = game["game_img_full"]

        display_name = mongo.db.users.find_one(
            {"username": session["user"]})["display_name"]

        date = datetime.datetime.now()

        review = {
            "game_title": title,
            "game_img_full": img_full,
            "platform": request.form.get("platform-select").lower(),
            "summary": request.form.get("summary"),
            "gameplay_rating": request.form.get("gameplay-stars"),
            "gameplay": request.form.get("gameplay"),
            "visuals_rating": request.form.get("visuals-stars"),
            "visuals": request.form.get("visuals"),
            "sound_rating": request.form.get("sound-stars"),
            "sound": request.form.get("sound"),
            "recommended": request.form.get("radioRecommend"),
            "date_submitted": date.strftime("%x"),
            "username": session["user"],
            "display_name": display_name
        }

        # Check if a user has already added a game with the same to the db
        existing_review = mongo.db.user_reviews.find_one(
            {"$and": [{"username": session["user"]},
                      {"game_title": title}]})

        if existing_review is None:
            mongo.db.user_reviews.insert_one(review)
            flash("Review Successfully Submitted")

        elif existing_review:
            flash("You've Already Submitted a Review for this Game")

        else:
            mongo.db.user_reviews.insert_one(review)
            flash("Review Successfully Submitted")

        return redirect(url_for('reviews'))

    return render_template(
        "games-review_form.html", matching_results=games)


# ======================
# Profile- Submit Review
# ======================

@app.route("/submit-review/<game_id>", methods=["GET", "POST"])
def profile_submit_review(game_id):
    if request.method == "POST":

        title = request.form.get("query")
        game = mongo.db.all_pc_games.find_one({"game_title": title})
        img_full = game["game_img_full"]

        date = datetime.datetime.now()

        display_name = mongo.db.users.find_one(
            {"username": session["user"]})["display_name"]

        review = {
            "game_title": title,
            "game_img_full": img_full,
            "platform": request.form.get("platform-select").lower(),
            "summary": request.form.get("summary"),
            "gameplay_rating": request.form.get("gameplay-stars"),
            "gameplay": request.form.get("gameplay"),
            "visuals_rating": request.form.get("visuals-stars"),
            "visuals": request.form.get("visuals"),
            "sound_rating": request.form.get("sound-stars"),
            "sound": request.form.get("sound"),
            "recommended": request.form.get("radioRecommend"),
            "date_submitted": date.strftime("%x"),
            "username": session["user"],
            "display_name": display_name
        }

        # Check if a user has already added a game with the same to the db
        existing_review = mongo.db.user_reviews.find_one(
            {"$and": [{"username": session["user"]},
                      {"game_title": title}]})

        if existing_review is None:
            mongo.db.user_reviews.insert_one(review)
            flash("Review Successfully Submitted")

        elif existing_review:
            flash("You've Already Submitted a Review for this Game")

        else:
            mongo.db.user_reviews.insert_one(review)
            flash("Review Successfully Submitted")

        return redirect(url_for("reviews"))

    game = mongo.db.user_games.find_one({"_id": (ObjectId(game_id))})

    return render_template(
        "profile-review_form.html", matching_results=games, game=game,
        username=session["user"])


# =====================
# Profile - Edit Review
# =====================

@app.route("/edit-review/<game_id>", methods=["GET", "POST"])
def edit_review(game_id):
    game = mongo.db.user_games.find_one({"_id": (ObjectId(game_id))})

    game_title = game["game_title"]
    img_sm = game["game_img_sm"]
    img_full = game["game_img_full"]

    review = mongo.db.user_reviews.find_one(
            {"$and": [{"username": session["user"]},
                      {"game_title": game_title}]})

    review_id = review["_id"]
    submission_date = review["date_submitted"]

    if request.method == "POST":
        date = datetime.datetime.now()

        update = {
            "game_title": game_title,
            "game_img_sm": img_sm,
            "game_img_full": img_full,
            "platform": request.form.get("platform-select").lower(),
            "summary": request.form.get("summary"),
            "gameplay_rating": request.form.get("gameplay-stars"),
            "gameplay": request.form.get("gameplay"),
            "visuals_rating": request.form.get("visuals-stars"),
            "visuals": request.form.get("visuals"),
            "sound_rating": request.form.get("sound-stars"),
            "sound": request.form.get("sound"),
            "recommended": request.form.get("radioRecommend"),
            "date_submitted": submission_date,
            "last_updated": date.strftime("%x"),
            "username": session["user"]
        }
        mongo.db.user_reviews.update({"_id": review_id}, update)
        flash("Review Successfully Updated")
        return redirect(url_for('reviews'))

    return render_template(
        "games-edit_review.html", game=game, review=review)


# =============================
# Profile Reviews - Edit Review
# =============================

@app.route("/profile/edit-review/<review_id>", methods=["GET", "POST"])
def profile_edit_review(review_id):
    review = mongo.db.user_reviews.find_one({"_id": ObjectId(review_id)})

    game_title = review["game_title"]
    img_sm = review["game_img_sm"]
    img_full = review["game_img_full"]
    submission_date = review["date_submitted"]

    if request.method == "POST":
        date = datetime.datetime.now()

        update = {
            "game_title": game_title,
            "game_img_sm": img_sm,
            "game_img_full": img_full,
            "platform": request.form.get("platform-select").lower(),
            "summary": request.form.get("summary"),
            "gameplay_rating": request.form.get("gameplay-stars"),
            "gameplay": request.form.get("gameplay"),
            "visuals_rating": request.form.get("visuals-stars"),
            "visuals": request.form.get("visuals"),
            "sound_rating": request.form.get("sound-stars"),
            "sound": request.form.get("sound"),
            "recommended": request.form.get("radioRecommend"),
            "date_submitted": submission_date,
            "last_updated": date.strftime("%x"),
            "username": session["user"]
        }
        mongo.db.user_reviews.update({"_id": ObjectId(review_id)}, update)
        flash("Review Successfully Updated")
        return redirect(url_for('reviews'))

    return render_template(
        "profile-edit_review.html", review=review)


# ======================
# Profile- Delete Review
# ======================

@app.route("/delete-review/<review_id>")
def delete_review(review_id):
    mongo.db.user_reviews.remove({"_id": ObjectId(review_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for("profile_reviews", username=session["user"]))


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
