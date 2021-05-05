"""
    ** Attribution:

    * Adding Pagination:
    "https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9"

    * Finding all the values of a specific key within a collection:
    "https://stackoverflow.com/questions/34861949/how-to-find-all-values-for-a-specific-key-in-pymongo"

    * Redirecting users back to the same page:
    "https://stackoverflow.com/questions/41270855/flask-redirect-to-same-page-after-form-submission/41272173"

    * Getting the previous URL with Flask:
    "https://stackoverflow.com/questions/39777171/how-to-get-the-previous-url-in-flask"

    * Returning a random document from MongoDB collection:
    "https://stackoverflow.com/questions/2824157/random-record-from-mongodb"

    * Selecting a random item from a list:
    "https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list"

    * Returning documents from MongoDB without duplicates:
    "https://stackoverflow.com/questions/11470614/mongodb-return-all-documents-by-field-without-duplicates"

    * Add session cookies to browser with Flask:
    "https://pythonbasics.org/flask-cookies/"

    * For cache control, to help boost performance, I used the following code:
    "https://stackoverflow.com/questions/23112316/using-flask-how-do-i-modify-the-cache-control-header-for-all-output"

    * For using MongoDB $search phrase with a variable:
    "https://stackoverflow.com/questions/43779319/mongodb-text-search-exact-match-using-variable"

    * To use zip with Jinja:
    "https://thetopsites.net/article/53453426.shtml"

    * Check if ObjectId is valid:
    "https://stackoverflow.com/questions/28774526/how-to-check-that-mongo-objectid-is-valid-in-python"

"""

import os
import datetime
import random
import string
from flask.templating import render_template_string
import requests
from bs4 import BeautifulSoup
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for, make_response)
from flask_pymongo import PyMongo, pymongo
from flask_paginate import Pagination, get_page_args
from bson.objectid import ObjectId
from bson.json_util import dumps
from requests.api import get
from werkzeug.security import generate_password_hash, check_password_hash
from scrape_custom_links import custom_games
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 172800

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

app.jinja_env.filters['zip'] = zip

mongo = PyMongo(app)


# =============
# Cache Control
# =============

@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    if 'Cache-Control' not in response.headers:
        response.headers['Cache-Control'] = 'no-store'
    return response


# =============
# Base Template
# =============

@app.route("/base")
def base():
    return render_template("base.html")


# =============
# Navbar Search
# =============

@app.route("/nav-search", methods=["POST"])
def get_nav_query():
    # Grab query
    query = request.form.get("nav-query")
    return redirect(url_for('search', query=query))


# ====================
# Secondary Nav Search
# ====================

@app.route("/search", methods=["POST"])
def get_query():
    # Grab query
    query = request.form.get("query")
    return redirect(url_for('search', query=query))


# ======
# Search
# ======

@app.route("/search/<query>", methods=["GET"])
def search(query):
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    # Grab game data for autocomplete function
    gameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    if query is None:
        return redirect(url_for("pc_games"))

    mongo.db.all_pc_games.create_index([("game_title", "text")])
    games = mongo.db.all_pc_games.find(
        {"$text": {"$search": query}})

    # Set carousel images
    random_games = mongo.db.all_pc_games.aggregate([
        {"$match": {"favourite": True}},
        {"$sample": {"size": 3}}
    ])

    rand_games = []
    for game in random_games:
        rand_games.append(game)

    rand_game_1 = rand_games[0]
    rand_game_2 = rand_games[1]
    rand_game_3 = rand_games[2]

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
        "search_results.html", games=pagination_games,
        pagination=pagination, rand_game_1=rand_game_1,
        rand_game_2=rand_game_2, rand_game_3=rand_game_3,
        navGameData=navGameData, gameData=gameData)


# ==============
# Search Reviews
# ==============

@app.route("/community-reviews/search", methods=["POST"])
def get_review_query():
    query = request.form.get("review-query")
    return redirect(url_for('search_reviews', query=query))


@app.route("/community-reviews/search/<query>", methods=["GET"])
def search_reviews(query):
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    # Grab review data for autocomplete function
    reviewData = mongo.db.user_reviews.find({}).distinct("game_title")

    mongo.db.user_reviews.create_index([("game_title", "text")])
    reviews = mongo.db.user_reviews.find(
        {"$text": {"$search": query}})

    # Set carousel images
    random_games = mongo.db.all_pc_games.aggregate([
        {"$match": {"favourite": True}},
        {"$sample": {"size": 3}}
    ])

    rand_games = []
    for game in random_games:
        rand_games.append(game)

    rand_game_1 = rand_games[0]
    rand_game_2 = rand_games[1]
    rand_game_3 = rand_games[2]

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
        "reviews.html", game_reviews=pagination_game_reviews,
        pagination=pagination, rand_game_1=rand_game_1,
        rand_game_2=rand_game_2, rand_game_3=rand_game_3,
        navGameData=navGameData, reviewData=reviewData)


# ========
# Homepage
# ========

@app.route("/")
@app.route("/home")
def home():
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

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
        "index.html", bestsellers=pagination_bestsellers,
        pagination=pagination, awardwinners=awardwinners,
        navGameData=navGameData)


# =============================
# Admin Controls - See Requests
# =============================

@app.route("/admin/user-requests", methods=["GET", "POST"])
def admin_user_requests():
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    user_requests = mongo.db.game_requests.find()

    if request.method == "POST":
        session["navSelect1"] = request.form.get("navSelect1").lower()
        session["navSelect2"] = request.form.get("navSelect2").lower()

    navSelect1 = session["navSelect1"]
    navSelect2 = session["navSelect2"]

    # Sort filter

    if navSelect1 == "title" and navSelect2 == "desc":
        user_requests.sort("game_request", pymongo.DESCENDING)

    elif navSelect1 == "title" and navSelect2 == "asc":
        user_requests.sort("requested_by", pymongo.ASCENDING)

    elif navSelect1 == "user-count" and navSelect2 == "desc":
        user_requests.sort("requested_by", pymongo.DESCENDING)

    elif navSelect1 == "user-count" and navSelect2 == "asc":
        user_requests.sort("game_request", pymongo.ASCENDING)

    return render_template(
        "admin-user_requests.html", user_requests=user_requests,
        navSelect1=navSelect1, navSelect2=navSelect2, navGameData=navGameData)


# =============================
# Admin Controls - Add To Queue
# =============================

@app.route("/admin/user-requests/add-to-queue/<request_id>", methods=["GET", "POST"])
def admin_add_to_queue(request_id):
    if request.method == "POST":
        game_request = mongo.db.game_requests.find_one({"_id": ObjectId(request_id)})

        user = mongo.db.users.find_one({"username": session["user"]})

        # Check if passwords match
        password = request.form.get("password")
        confirm_password = request.form.get("confirmPassword")

        if password == confirm_password:
            # Check password
            if check_password_hash(user["password"], password):

                # Check if game already exisits in queue
                in_queue = mongo.db.game_queue.find_one(
                    {"game_link": game_request["game_link"]})

                # Check if game already exisits in games col
                existing_game = mongo.db.all_pc_games.find_one(
                    {"game_link": game_request["game_link"]})

                if in_queue:
                    flash("'{}' Already In Waiting List".format(game_request["game_request"]))
                    return redirect(url_for("admin_add_to_db"))

                if existing_game:
                    flash("'{}' Already Exists in Our Database".format(game_request["game_request"]))
                    return redirect(url_for("admin_user_requests"))
                
                # Otherwise add to db
                game = {
                    "game_title": game_request["game_request"],
                    "game_link": game_request["game_link"],
                    "category": request.form.getlist("category")
                }
                mongo.db.game_queue.insert_one(game)
                flash("Succesfully Added '{}' To Queue".format(game_request["game_request"]))
                return redirect(url_for("admin_user_requests"))
            else:
                flash("Details Invalid")
                return redirect(url_for("admin_user_requests"))
        else:
            flash("Details Invalid")
            return redirect(url_for("admin_user_requests"))


# ===========================
# Admin Controls - Game Queue
# ===========================

@app.route("/admin/game-queue")
def admin_game_queue():
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    games = mongo.db.game_queue.find()
    
    # Remove games from queue that have been added to the games col
    def remove_added_games():
        games = mongo.db.game_queue.find()
        existing_games = mongo.db.all_pc_games.find()

        existing_game_links = []
        game_links = []
        matches = []

        # Sort through data and add to empty arrays
        for i in list(existing_games):
            existing_game_links.append(i["game_link"])

        for i in list(games):
            game_links.append(i["game_link"])

        # Find matches
        for i in existing_game_links:
            for x in game_links:
                if i == x:
                    matches.append(x)

        # Remove from game queue col
        for link in matches:
            game = mongo.db.game_queue.find_one({"game_link": link})
            mongo.db.game_queue.remove({"_id": game["_id"]})


    remove_added_games()

    return render_template(
        "admin-game_queue.html", navGameData=navGameData,
        games=games)


# ==========================
# Admin Controls - Update DB
# ==========================

@app.route("/admin/update-db", methods=["GET", "POST"])
def admin_update_db():
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    if request.method == "POST":
        user = mongo.db.users.find_one({"username": session["user"]})

        # Check if passwords match
        password = request.form.get("password")
        confirm_password = request.form.get("confirmPassword")

        if password == confirm_password:
            # Check password
            if check_password_hash(user["password"], password):
                # Update DB
                for k, v in custom_games.items():
                    game = v
                    title = game["game_title"]

                    existing_game = mongo.db.all_pc_games.find_one(
                        {"game_title": title})

                if not existing_game:
                    mongo.db.all_pc_games.insert_one(game)

                if existing_game:
                    flash("Database Already Updated")
                    return redirect(url_for("home"))

                if not existing_game:
                    flash("Successfully Updated Database")
                    return redirect(url_for("home"))

            else:
                flash("Details Invalid")
        else:
            flash("Details Invalid")

    return render_template("admin-update_db.html", navGameData=navGameData)


# ===============================
# Admin Controls - Remove Request
# ===============================

@app.route("/admin/user-requests/remove-request/<request_id>", methods=["GET", "POST"])
def admin_remove_request(request_id):
    user_request = mongo.db.game_requests.find_one(
        {"_id": ObjectId(request_id)})

    request_title = user_request["game_request"]

    games = mongo.db.all_pc_games.find_one(
        {"$text": {"$search": "(\"{}\"".format(request_title)}})

    if not games:
        flash("Error! Games that do not exist within the database cannot be removed")

    if games:
        mongo.db.game_requests.remove({"_id": ObjectId(request_id)})
        flash("User Requested Deleted")
        return redirect(url_for("admin_user_requests"))

    return redirect(url_for("admin_user_requests"))


# ===================
# Game pages template
# ===================

@app.route("/games")
def games_template():
    return render_template("games-template.html")


# =================
# Games Sort Filter
# =================

@app.route("/setcookie", methods=["GET", "POST"])
def setcookie_all():
    # Get parameters for game page
    page = request.referrer
    page_param = page.split("games/")
    genre = page_param[1]

    if request.method == "POST":
        cookie1 = request.form.get("navSelect1").lower()
        cookie2 = request.form.get("navSelect2").lower()

        resp = make_response(redirect(url_for("games", genre=genre)))
        resp.set_cookie("navSelect1", cookie1)
        resp.set_cookie("navSelect2", cookie2)

        return resp


# ================
# Game Genre - All
# ================

@app.route("/all-games", methods=["POST", "GET"])
def all_games():
    genre = "all-games"
    return redirect(url_for("games", genre=genre))


# ===================
# Game Genre - Action
# ===================

@app.route("/action-games", methods=["POST", "GET"])
def action_games():
    genre = "action"
    return redirect(url_for("games", genre=genre))


# ======================
# Game Genre - Adventure
# ======================

@app.route("/adventure-games", methods=["POST", "GET"])
def adventure_games():
    genre = "adventure"
    return redirect(url_for("games", genre=genre))


# ===================
# Game Genre - RPG
# ===================

@app.route("/rpg-games", methods=["POST", "GET"])
def rpg_games():
    genre = "rpg"
    return redirect(url_for("games", genre=genre))


# =====================
# Game Genre - Strategy
# =====================

@app.route("/strategy-games", methods=["POST", "GET"])
def strategy_games():
    genre = "strategy"
    return redirect(url_for("games", genre=genre))


# ========================
# Game Genre - Multiplayer
# ========================

@app.route("/multiplayer-games", methods=["POST", "GET"])
def multiplayer_games():
    genre = "multiplayer"
    return redirect(url_for("games", genre=genre))


# =====
# Games
# =====

@app.route("/games/<genre>", methods=["GET", "POST"])
def games(genre):
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    # Grab game data for autocomplete function
    gameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    # Set carousel images
    random_games = mongo.db.all_pc_games.aggregate([
        {"$match": {"favourite": True}},
        {"$sample": {"size": 3}}
    ])

    rand_games = []
    for game in random_games:
        rand_games.append(game)

    rand_game_1 = rand_games[0]
    rand_game_2 = rand_games[1]
    rand_game_3 = rand_games[2]

    # Get game results
    if genre == "all-games":
        game_results = mongo.db.all_pc_games.find()
    elif genre == "action":
        game_results = mongo.db.all_pc_games.find(
            {"$or": [{"action": True}, {"game_top_tags": "Action"}]})
    elif genre == "adventure":
        game_results = mongo.db.all_pc_games.find(
            {"$or": [{"adventure": True}, {"game_top_tags": "Adventure"}]})
    elif genre == "rpg":
        game_results = mongo.db.all_pc_games.find(
            {"$or": [{"RPG": True}, {"game_top_tags": "RPG"}]})
    elif genre == "strategy":
        game_results = mongo.db.all_pc_games.find(
            {"$or": [{"strategy": True}, {"game_top_tags": "Strategy"}]})
    elif genre == "multiplayer":
        game_results = mongo.db.all_pc_games.find(
            {"$or": [{"multiplayer": True}, {"game_top_tags": "Multiplayer"}]})

    # Pagination
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    per_page = 6
    offset = ((page - 1) * per_page)

    total = game_results.count()
    pagination_games = game_results[offset: offset + per_page]

    pagination = Pagination(
        page=page, per_page=per_page, total=total,
        css_framework='materialize')

    # Find site favourites
    favourites = list(mongo.db.all_pc_games.find({"favourite": True}))

    # Sort filter
    cookie1 = request.cookies.get("navSelect1")
    cookie2 = request.cookies.get("navSelect2")

    if cookie1 is None and cookie2 is None:
        navSelect1 = "default"
        navSelect2 = "desc"
    else:
        navSelect1 = cookie1
        navSelect2 = cookie2

    # Sort by Likes

    if navSelect1 == "likes" and navSelect2 == "desc":
        pagination_games.sort("likes", pymongo.DESCENDING)

    elif navSelect1 == "likes" and navSelect2 == "asc":
        pagination_games.sort("likes", pymongo.ASCENDING)

    # Sort by game title
    elif navSelect1 == "title" and navSelect2 == "desc":
        pagination_games.sort("game_title", pymongo.DESCENDING)

    elif navSelect1 == "title" and navSelect2 == "asc":
        pagination_games.sort("game_title", pymongo.ASCENDING)

    # Sort by bestseller
    elif navSelect1 == "bestseller" and navSelect2 == "desc":
        pagination_games.sort("bestseller", pymongo.DESCENDING)

    elif navSelect1 == "bestseller" and navSelect2 == "asc":
        pagination_games.sort("bestseller", pymongo.ASCENDING)

    # Sort by awardwinner
    elif navSelect1 == "awardwinner" and navSelect2 == "desc":
        pagination_games.sort("awardwinner", pymongo.DESCENDING)

    elif navSelect1 == "awardwinner" and navSelect2 == "asc":
        pagination_games.sort("awardwinner", pymongo.ASCENDING)

    # Sort by favourite
    elif navSelect1 == "favourite" and navSelect2 == "desc":
        pagination_games.sort("favourite", pymongo.DESCENDING)

    elif navSelect1 == "favourite" and navSelect2 == "asc":
        pagination_games.sort("favourite", pymongo.ASCENDING)

    return render_template(
        "games.html", navGameData=navGameData,
        gameData=gameData, rand_game_1=rand_game_1,
        rand_game_2=rand_game_2, rand_game_3=rand_game_3,
        games=pagination_games, pagination=pagination,
        favourites=favourites, navSelect1=navSelect1,
        navSelect2=navSelect2)


# ===================
# Award Winner Games
# ===================

@app.route("/games/awardwinners", methods=["GET", "POST"])
def awardwinner_games():
    # Set carousel images
    random_games = mongo.db.all_pc_games.aggregate([
        {"$match": {"favourite": True}},
        {"$sample": {"size": 3}}
    ])

    rand_games = []
    for game in random_games:
        rand_games.append(game)

    rand_game_1 = rand_games[0]
    rand_game_2 = rand_games[1]
    rand_game_3 = rand_games[2]

    # Find games
    pc_games = mongo.db.all_pc_games.find({"awardwinner": True})

    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    # Grab game data for autocomplete function
    gameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    # Pagination
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
    favourites = list(mongo.db.all_pc_games.find({"favourite": True}))

    return render_template(
        "games-awardwinners.html", pc_games=pagination_pc_games,
        pagination=pagination, favourites=favourites,
        rand_game_1=rand_game_1, rand_game_2=rand_game_2,
        rand_game_3=rand_game_3, navGameData=navGameData,
        gameData=gameData)


# ===============================
# Games Sort Filter - Favourites
# ===============================

@app.route("/setcookie/favourites", methods=["GET", "POST"])
def setcookie_favourites():
    if request.method == "POST":
        cookie1 = request.form.get("navSelect1").lower()
        cookie2 = request.form.get("navSelect2").lower()

        resp = make_response(redirect(url_for("favourites")))
        resp.set_cookie("navSelect1", cookie1)
        resp.set_cookie("navSelect2", cookie2)

        return resp


# =================
# Site's Favourites
# =================

@app.route("/our-favourites", methods=["GET", "POST"])
def favourites():
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

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

    # Sort filter

    cookie1 = request.cookies.get("navSelect1")
    cookie2 = request.cookies.get("navSelect2")

    if cookie1 is None and cookie2 is None:
        navSelect1 = "likes"
        navSelect2 = "desc"
    else:
        navSelect1 = cookie1
        navSelect2 = cookie2

    # Sort by Likes

    if navSelect1 == "likes" and navSelect2 == "desc":
        favourites.sort("likes", pymongo.DESCENDING)

    elif navSelect1 == "likes" and navSelect2 == "asc":
        favourites.sort("likes", pymongo.ASCENDING)

    # Sort by game title
    elif navSelect1 == "title" and navSelect2 == "desc":
        favourites.sort("game_title", pymongo.DESCENDING)

    elif navSelect1 == "title" and navSelect2 == "asc":
        favourites.sort("game_title", pymongo.ASCENDING)

    return render_template(
        "games-favourites.html", favourites=favourites,
        rand_game_title=rand_game_title, rand_game_imgs=rand_game_imgs,
        rand_game_summary=rand_game_summary, rand_game_id=rand_game_id,
        navSelect1=navSelect1, navSelect2=navSelect2, navGameData=navGameData)


# ==========
# Register
# ==========

@app.route("/register", methods=["GET", "POST"])
def register():
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

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
            session["admin"] = False
            flash("Registration Successful")
            return redirect(url_for("profile_games", username=session["user"]))

    return render_template("register.html", navGameData=navGameData)


# ==========
# Login
# ==========

@app.route("/login", methods=["GET", "POST"])
def login():
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    if request.method == "POST":
        # Check if email exists in the db
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            # Check if hashed password matches user input
            if check_password_hash(
               existing_user["password"], request.form.get("password")):

                # Get username
                username = existing_user["username"]
                # Create session cookie for user
                session["user"] = username

                # Create session cookie for admin
                user = mongo.db.users.find_one({"username": username})
                admin = user["admin"]

                if admin is True:
                    session["admin"] = True
                else:
                    session["admin"] = False

                # Success - redirect to profile
                flash("Welcome {}".format(username.capitalize()))
                return redirect(url_for(
                    "profile_games", username=session["user"]))
            else:
                # Invalid password match
                flash("Incorrect Email and/or Password")
                return redirect(url_for("login"))
        else:
            # Invalid password match
            flash("Incorrect Email and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html", navGameData=navGameData)


# ==========
# Game Likes
# ==========

@app.route("/like/<game_id>")
def like(game_id):
    # Grab game data from database
    game = mongo.db.all_pc_games.find_one({"_id": ObjectId(game_id)})

    # Find username
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    # Check if a user has already liked the game
    already_liked = game["liked_by"]

    # If 'liked_by' is null
    if already_liked is None:
        # Add like
        like = {"$set": {
            "likes": 1,
            "liked_by": [username]
        }}
        mongo.db.all_pc_games.update_one({"_id": ObjectId(game_id)}, like)
        flash("Liked added!")
        return redirect(request.referrer)
    # Else check if session user has already liked the game
    elif username in already_liked:
        flash("Sorry, but you've already liked this game.")
        return redirect(request.referrer)

    # If game has never been liked
    if game["likes"] == int(0):
        # Add like
        like = {"$set": {
            "likes": 1,
            "liked_by": [username]
        }}
        mongo.db.all_pc_games.update_one({"_id": ObjectId(game_id)}, like)
        flash("Liked added!")
        return redirect(request.referrer)

    # If game already has likes
    else:
        # Find game likes total
        like_num = mongo.db.all_pc_games.find_one(
            {"_id": ObjectId(game_id)})["likes"]

        new_like_num = int(like_num) + 1

        # Update like total and add session user to 'liked_by'
        like = {
            "$set": {
                "likes": new_like_num
            },
            "$push": {
                "liked_by": username
            }
        }
        mongo.db.all_pc_games.update_one(
            {"_id": ObjectId(game_id)}, like, upsert=False)
        flash("Liked added!")
        return redirect(request.referrer)


# ==============
# Request A Game
# ==============

@app.route("/request-a-game", methods=["GET", "POST"])
def request_game():
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    # Post game request
    if request.method == "POST":
        game_request = request.form.get("game-request").lower()

        # Deconstruct the string so that it's suitable for the url
        request_str = game_request.translate(str.maketrans(
            '', '', string.punctuation))
        request_str = request_str.replace(" ", "+")

        link = ""

        # Search for string on the Steam Store website
        base_url = "https://store.steampowered.com/search/?term="
        url = base_url + request_str

        cookies = {"birthtime": "786240001", "lastagecheckage": "1-0-1995"}
        source = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(source.text, "html.parser")

        # -------------------------------------------------- Game Links
        try:
            a = soup.find(
                'a', {'class': 'search_result_row ds_collapse_flag'})['href']

            split_href = a.split("?")
            link = split_href[0]

            title = soup.find("span", {"class": "title"}).text

        except TypeError:
            link = "no results"

        # If the game does not exist on Steam
        if link == "no results":
            flash(
                "Sorry, we can't find any results for '{}'".format(
                    game_request.title()))

        # Otherwise add game request to db
        else:
            return redirect(url_for(
                "confirm_request", game_request=game_request,
                title=title))

    return render_template("request_form.html", navGameData=navGameData)


# ======================
# Request A Game - Modal
# ======================

@app.route("/request-a-game/request=<game_request>/found=<title>", methods=["GET", "POST"])
def confirm_request(game_request, title):
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    if request.method == "POST":
        # -------------------------------------------------- Get Steam Link

        # Deconstruct the string so that it's suitable for the url
        game_request.lower()
        request_str = game_request.translate(str.maketrans(
            '', '', string.punctuation))
        request_str = request_str.replace(" ", "+")

        link = ""

        # Search for string on the Steam Store website
        base_url = "https://store.steampowered.com/search/?term="
        url = base_url + request_str

        cookies = {"birthtime": "786240001", "lastagecheckage": "1-0-1995"}
        source = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(source.text, "html.parser")

        a = soup.find(
            'a', {'class': 'search_result_row ds_collapse_flag'})['href']

        split_href = a.split("?")
        link = split_href[0]

        # -------------------------------------------------- Update DB

        # Grab session user's username
        user = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        # Check if game request already exisit in db
        exisiting_game = mongo.db.all_pc_games.find_one({"game_link": link})

        # Check if game has already been requested
        existing_request = mongo.db.game_requests.find_one(
            {"game_request": title})

        if exisiting_game:
            flash("Error! '{}' already exists in our database".format(title))
            return redirect(url_for("request_game"))

        if existing_request is not None:
            has_user_requested = existing_request["requested_by"]

            # Block users from requesting the same game
            if user in has_user_requested:
                flash(
                    "You've already submitted a request for '{}'. Don't worry, we haven't forgot about it!".format(title))
                return redirect(url_for("request_game"))

            # Update existing game request with session user's username
            if existing_request:
                # Find id of document
                request_id = existing_request["_id"]
                # Update existing document
                mongo.db.game_requests.update_one(
                    {"_id": request_id},
                    {"$push": {"requested_by": user}})

                flash(
                    "Thanks! We've Submitted your Request for '{}'".format(title))
                return redirect(url_for("home"))

        # Else add new document
        game = {
            "game_request": title,
            "game_link": link,
            "requested_by": [user]
        }
        mongo.db.game_requests.insert_one(game)

        flash(
            "Thanks! We've Submitted your Request for '{}'".format(
                game_request.title()))
        return redirect(url_for("home"))

    return render_template(
        "request_form-modal.html", navGameData=navGameData,
        game_request=game_request, title=title)


# =============================
# Add game to Profile Game List
# =============================

@app.route("/add_game/<game_id>")
def add_game(game_id):

    # Check if ObjectId is valid
    if ObjectId.is_valid(game_id):
        game = mongo.db.all_pc_games.find_one({"_id": ObjectId(game_id)})
    else:
        game = mongo.db.all_pc_games.find_one({"game_title": game_id})

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
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

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
        "profile-edit_general.html", username=session["user"], user=user,
        navGameData=navGameData)


# =======================
# Edit Profile - Password
# =======================

@app.route(
    "/edit-profile/<username>/general/password-reset", methods=["GET", "POST"])
def edit_password(username):
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    user = mongo.db.users.find_one({"username": session["user"]})
    if request.method == "POST":
        user_id = user["_id"]

        # Check password
        if check_password_hash(user["password"], request.form.get("password")):

            # Check if new passwords match
            new_password = request.form.get("change-password")
            confirm_new_password = request.form.get("confirm-new-password")

            if new_password == confirm_new_password:
                # Update db
                update = {"$set": {
                    "password": generate_password_hash(new_password)
                }}
                mongo.db.users.update_one({"_id": user_id}, update)
                flash("Password Successfully Updated")
                return redirect(url_for(
                    "profile_games", username=session["user"]))

            else:
                # Invalid match
                flash("Inputs invalid")
                return redirect(url_for(
                    "edit_password", username=session["user"]))
        else:
            # Invalid password
            flash("Password Incorrect")
            return redirect(url_for("edit_password", username=session["user"]))

    return render_template(
        "profile-edit_password.html", username=session["user"], user=user,
        navGameData=navGameData)


# =====================
# Edit Profile - Avatar
# =====================

@app.route("/edit-profile/<username>/avatar")
def edit_profile_avatar(username):
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    user_data = mongo.db.users.find()
    avatars = mongo.db.avatars.find().sort("img_alt", 1)
    return render_template(
        "profile-edit_avatar.html", username=session["user"],
        user_data=user_data, avatars=avatars, navGameData=navGameData)


# ============================
# Edit Profile - Update Avatar
# ============================

@app.route("/update-avatar/<avatar_id>", methods=["GET", "POST"])
def update_avatar(avatar_id):
    if request.method == "POST":
        # Grab user id and avatar
        user_id = mongo.db.users.find_one({"username": session["user"]})["_id"]
        avatar = mongo.db.avatars.find({"_id": ObjectId(avatar_id)})

        # Grab avatar img path and alt attribute
        for i in list(avatar):
            img_path = i["img_path"]
            img_alt = i["img_alt"]

        # Update avatar
        update = {"$set": {
            "avatar": img_path,
            "avatar_desc": img_alt
        }}
        mongo.db.users.update({"_id": user_id}, update)
        flash("Avatar Successfully Updated")

    return redirect(url_for("edit_profile_avatar", username=session["user"]))


# =====================
#  Profile - Game Likes
# =====================

@app.route("/profile/<username>/likes")
def profile_likes(username):
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    # Find session user
    user = mongo.db.users.find_one({"username": session["user"]})
    username = user["username"]
    # Find games
    games = mongo.db.all_pc_games.find({"liked_by": username})
    return render_template(
        "profile-game_likes.html", user=user, games=games,
        navGameData=navGameData)


# ====================
# Profile - Games List
# ====================

@app.route("/profile/<username>")
def profile_games(username):
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    # Find session user
    user = mongo.db.users.find_one({"username": session["user"]})

    # Grab username
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
        games_completed=games_completed, matches=matches,
        navGameData=navGameData)


# =========================
# Profile - Move to Playing
# =========================

@app.route("/play-now/<game_id>", methods=["GET", "POST"])
def game_to_playing(game_id):
    if request.method == "POST":
        # Set 'stage' value to 'playing'
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
        # Set 'stage' value to 'next'
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
        # Set 'stage' value to 'completed'
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
    # Remove game from playlist
    mongo.db.user_games.remove({"_id": ObjectId(game_id)})
    flash("Game Successfully Removed from Your List")
    return redirect(url_for("profile_games", username=session["user"]))


# ======================
# Visit Profile Template
# ======================

@app.route("/profiles-template")
def profiles_template():
    return render_template(
        "visit_profile-template.html")


# ==============
# Visit Profiles
# ==============

@app.route("/profiles/<user>")
def profiles(user):
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    # Find the user's game playlist
    user_games = mongo.db.user_games.find({"username": user})
    games_playing = mongo.db.user_games.find({"stage": "playing"})
    games_next = mongo.db.user_games.find({"stage": "next"})
    games_completed = mongo.db.user_games.find({"stage": "completed"})

    # Find user reviews
    user_reviews = mongo.db.user_reviews.find({"username": user})

    # Find game likes
    game_likes = mongo.db.all_pc_games.find({"liked_by": user})

    # Find user details
    user_data = mongo.db.users.find_one({"username": user})
    username = user_data["username"]
    user_display_name = user_data["display_name"]
    user_avatar = user_data["avatar"]

    # Find game titles
    user_game_titles = []
    for i in list(user_games):
        user_game_titles.append(i["game_title"])

    # Find review game titles
    user_game_reviews = []
    for i in list(user_reviews):
        user_game_reviews.append(i["game_title"])

    # Find game likes
    user_game_likes = []
    for i in list(game_likes):
        user_game_likes.append(i["game_title"])

    # Find matches
    review_matches = []
    for i in user_game_titles:
        for x in user_game_reviews:
            if i == x:
                review_matches.append(x)

    # Find matches
    like_matches = []
    for i in user_game_titles:
        for x in user_game_likes:
            if i == x:
                like_matches.append(x)

    # Find session user's game list
    session_user_games = mongo.db.user_games.find(
        {"username": session["user"]}).distinct("game_title")

    return render_template(
        "visit_profile-games_list.html",
        games_playing=games_playing, games_next=games_next,
        games_completed=games_completed, user=user,
        username=username, user_display_name=user_display_name,
        user_avatar=user_avatar, review_matches=review_matches,
        like_matches=like_matches, session_user_games=session_user_games,
        navGameData=navGameData)


# ======================
# Visit Profiles - Likes
# ======================

@app.route("/profiles/<user>/likes")
def profiles_likes(user):
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    # Find user details
    user_data = mongo.db.users.find_one({"username": user})
    username = user_data["username"]
    user_display_name = user_data["display_name"]
    user_avatar = user_data["avatar"]

    # Find games liked by the user
    user_liked_games = mongo.db.all_pc_games.find({"liked_by": user})

    return render_template(
        "visit_profile-game_likes.html", user=user,
        username=username, user_display_name=user_display_name,
        user_avatar=user_avatar, user_liked_games=user_liked_games,
        navGameData=navGameData)


# ========================
# Visit Profiles - Reviews
# ========================

@app.route("/profiles/<user>/reviews")
def profiles_reviews(user):
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    # Find user details
    user_data = mongo.db.users.find_one({"username": user})
    username = user_data["username"]
    user_display_name = user_data["display_name"]
    user_avatar = user_data["avatar"]

    # Find the user's reviews
    user_reviews = mongo.db.user_reviews.find({"username": user})

    return render_template(
        "visit_profile-reviews.html", user=user,
        username=username, user_display_name=user_display_name,
        user_avatar=user_avatar, user_reviews=user_reviews,
        navGameData=navGameData)


# ================
# Reviews Template
# ================

@app.route("/reviews")
def reviews_template():
    return render_template("reviews-template.html")


# ================
# See Game Reviews
# ================

@app.route("/community-reviews/<game_id>")
def see_game_reviews(game_id):
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    # Grab review data for autocomplete function
    reviewData = mongo.db.user_reviews.find({}).distinct("game_title")

    # Check if ObjectId is valid
    if ObjectId.is_valid(game_id):
        game = mongo.db.all_pc_games.find_one({"_id": ObjectId(game_id)})
    else:
        game = mongo.db.all_pc_games.find_one({"game_title": game_id})

    # Grab game details
    game_title = game["game_title"]
    game_img = game["game_img_full"]
    game_tags = game["game_top_tags"]

    # Filter reviews
    reviews = mongo.db.user_reviews.find({"game_title": game_title})

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

    # Set carousel images
    random_games = mongo.db.all_pc_games.aggregate([
        {"$match": {"favourite": True}},
        {"$sample": {"size": 3}}
    ])

    rand_games = []
    for game in random_games:
        rand_games.append(game)

    rand_game_1 = rand_games[0]
    rand_game_2 = rand_games[1]
    rand_game_3 = rand_games[2]

    return render_template(
        "reviews.html", game_reviews=pagination_game_reviews,
        pagination=pagination, rand_game_1=rand_game_1,
        rand_game_2=rand_game_2, rand_game_3=rand_game_3,
        reviewData=reviewData, game=game, game_img=game_img,
        game_tags=game_tags, navGameData=navGameData)


# ===================
# Reviews Sort Filter
# ===================

@app.route("/set-reviewcookie", methods=["GET", "POST"])
def set_review_cookies():
    if request.method == "POST":
        cookie1 = request.form.get("reviewSort1").lower()
        cookie2 = request.form.get("reviewSort2").lower()

        resp = make_response(redirect(url_for("reviews")))
        resp.set_cookie("reviewSort1", cookie1)
        resp.set_cookie("reviewSort2", cookie2)

        return resp


# ==========
# Reviews
# ==========

@app.route("/community-reviews", methods=["GET", "POST"])
def reviews():
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    # Find reviews
    game_reviews = mongo.db.user_reviews.find()

    # Grab review data for autocomplete function
    reviewData = mongo.db.user_reviews.find({}).distinct("game_title")

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

    # Sort filter

    cookie1 = request.cookies.get("reviewSort1")
    cookie2 = request.cookies.get("reviewSort2")

    if cookie1 is None and cookie2 is None:
        reviewSort1 = "date"
        reviewSort2 = "desc"
    else:
        reviewSort1 = cookie1
        reviewSort2 = cookie2

    # Sort by date added
    if reviewSort1 == "date" and reviewSort2 == "desc":
        pagination_game_reviews.sort("date_submitted", -1)

    elif reviewSort1 == "date" and reviewSort2 == "asc":
        pagination_game_reviews.sort("date_submitted", 1)

    # Sort by game title
    elif reviewSort1 == "title" and reviewSort2 == "desc":
        pagination_game_reviews.sort("game_title", pymongo.DESCENDING)

    elif reviewSort1 == "title" and reviewSort2 == "asc":
        pagination_game_reviews.sort("game_title", pymongo.ASCENDING)

    # Sort by rating
    elif reviewSort1 == "rating" and reviewSort2 == "desc":
        pagination_game_reviews.sort("recommended", -1)

    elif reviewSort1 == "rating" and reviewSort2 == "asc":
        pagination_game_reviews.sort("recommended", 1)

    # Set carousel images
    random_games = mongo.db.all_pc_games.aggregate([
        {"$match": {"favourite": True}},
        {"$sample": {"size": 3}}
    ])

    rand_games = []
    for game in random_games:
        rand_games.append(game)

    rand_game_1 = rand_games[0]
    rand_game_2 = rand_games[1]
    rand_game_3 = rand_games[2]

    return render_template(
        "reviews.html", game_reviews=pagination_game_reviews,
        pagination=pagination, reviewSort1=reviewSort1,
        reviewSort2=reviewSort2, rand_game_1=rand_game_1,
        rand_game_2=rand_game_2, rand_game_3=rand_game_3,
        reviewData=reviewData, navGameData=navGameData)


# ================
# Reviews - Action
# ================

@app.route("/community-reviews/action")
def reviews_action():
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    # Grab review data for autocomplete function
    reviewData = mongo.db.user_reviews.find({}).distinct("game_title")

    # Find action game titles
    action_games = mongo.db.all_pc_games.find({"action": True})
    titles = []
    for game in action_games:
        titles.append(game["game_title"])

    # Find reviews that match action game titles
    game_reviews = mongo.db.user_reviews.find({"game_title": {"$in": titles}})

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

    # Set carousel images
    random_games = mongo.db.all_pc_games.aggregate([
        {"$match": {"favourite": True}},
        {"$sample": {"size": 3}}
    ])

    rand_games = []
    for game in random_games:
        rand_games.append(game)

    rand_game_1 = rand_games[0]
    rand_game_2 = rand_games[1]
    rand_game_3 = rand_games[2]

    return render_template(
        "reviews.html", game_reviews=pagination_game_reviews,
        pagination=pagination, rand_game_1=rand_game_1,
        rand_game_2=rand_game_2, rand_game_3=rand_game_3,
        reviewData=reviewData, navGameData=navGameData)


# ===================
# Reviews - Adventure
# ===================

@app.route("/community-reviews/adventure")
def reviews_adventure():
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    # Grab review data for autocomplete function
    reviewData = mongo.db.user_reviews.find({}).distinct("game_title")

    # Find adventure game titles
    adventure_games = mongo.db.all_pc_games.find({"adventure": True})
    titles = []
    for game in adventure_games:
        titles.append(game["game_title"])

    # Find reviews that match adventure game titles
    game_reviews = mongo.db.user_reviews.find({"game_title": {"$in": titles}})

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

    # Set carousel images
    random_games = mongo.db.all_pc_games.aggregate([
        {"$match": {"favourite": True}},
        {"$sample": {"size": 3}}
    ])

    rand_games = []
    for game in random_games:
        rand_games.append(game)

    rand_game_1 = rand_games[0]
    rand_game_2 = rand_games[1]
    rand_game_3 = rand_games[2]

    return render_template(
        "reviews.html", game_reviews=pagination_game_reviews,
        pagination=pagination, rand_game_1=rand_game_1,
        rand_game_2=rand_game_2, rand_game_3=rand_game_3,
        reviewData=reviewData, navGameData=navGameData)


# =============
# Reviews - RPG
# =============

@app.route("/community-reviews/RPG")
def reviews_RPG():
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    # Grab review data for autocomplete function
    reviewData = mongo.db.user_reviews.find({}).distinct("game_title")

    # Find RPG game titles
    RPG_games = mongo.db.all_pc_games.find({"RPG": True})
    titles = []
    for game in RPG_games:
        titles.append(game["game_title"])

    # Find reviews that match RPG game titles
    game_reviews = mongo.db.user_reviews.find({"game_title": {"$in": titles}})

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

    # Set carousel images
    random_games = mongo.db.all_pc_games.aggregate([
        {"$match": {"favourite": True}},
        {"$sample": {"size": 3}}
    ])

    rand_games = []
    for game in random_games:
        rand_games.append(game)

    rand_game_1 = rand_games[0]
    rand_game_2 = rand_games[1]
    rand_game_3 = rand_games[2]

    return render_template(
        "reviews.html", game_reviews=pagination_game_reviews,
        pagination=pagination, rand_game_1=rand_game_1,
        rand_game_2=rand_game_2, rand_game_3=rand_game_3,
        reviewData=reviewData, navGameData=navGameData)


# ==================
# Reviews - Strategy
# ==================

@app.route("/community-reviews/strategy")
def reviews_strategy():
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    # Grab review data for autocomplete function
    reviewData = mongo.db.user_reviews.find({}).distinct("game_title")

    # Find strategy game titles
    strategy_games = mongo.db.all_pc_games.find({"strategy": True})
    titles = []
    for game in strategy_games:
        titles.append(game["game_title"])

    # Find reviews that match strategy game titles
    game_reviews = mongo.db.user_reviews.find({"game_title": {"$in": titles}})

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

    # Set carousel images
    random_games = mongo.db.all_pc_games.aggregate([
        {"$match": {"favourite": True}},
        {"$sample": {"size": 3}}
    ])

    rand_games = []
    for game in random_games:
        rand_games.append(game)

    rand_game_1 = rand_games[0]
    rand_game_2 = rand_games[1]
    rand_game_3 = rand_games[2]

    return render_template(
        "reviews.html", game_reviews=pagination_game_reviews,
        pagination=pagination, rand_game_1=rand_game_1,
        rand_game_2=rand_game_2, rand_game_3=rand_game_3,
        reviewData=reviewData, navGameData=navGameData)


# =====================
# Reviews - Multiplayer
# =====================

@app.route("/community-reviews/multiplayer")
def reviews_multiplayer():
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    # Grab review data for autocomplete function
    reviewData = mongo.db.user_reviews.find({}).distinct("game_title")

    # Find multiplayer game titles
    multiplayer_games = mongo.db.all_pc_games.find({"multiplayer": True})
    titles = []
    for game in multiplayer_games:
        titles.append(game["game_title"])

    # Find reviews that match multiplayer game titles
    game_reviews = mongo.db.user_reviews.find({"game_title": {"$in": titles}})

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

    # Set carousel images
    random_games = mongo.db.all_pc_games.aggregate([
        {"$match": {"favourite": True}},
        {"$sample": {"size": 3}}
    ])

    rand_games = []
    for game in random_games:
        rand_games.append(game)

    rand_game_1 = rand_games[0]
    rand_game_2 = rand_games[1]
    rand_game_3 = rand_games[2]

    return render_template(
        "reviews.html", game_reviews=pagination_game_reviews,
        pagination=pagination, rand_game_1=rand_game_1,
        rand_game_2=rand_game_2, rand_game_3=rand_game_3,
        reviewData=reviewData, navGameData=navGameData)


# =====================
# Reviews - PC Platform
# =====================

@app.route("/community-reviews/pc")
def reviews_pc():
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    # Grab review data for autocomplete function
    reviewData = mongo.db.user_reviews.find({}).distinct("game_title")

    # Find reviews with pc platform
    # Steam, Windows, Mac or Linux
    game_reviews = mongo.db.user_reviews.find({
        "platform": {"$in": ["windows", "mac", "linux", "steam"]}})

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

    # Set carousel images
    random_games = mongo.db.all_pc_games.aggregate([
        {"$match": {"favourite": True}},
        {"$sample": {"size": 3}}
    ])

    rand_games = []
    for game in random_games:
        rand_games.append(game)

    rand_game_1 = rand_games[0]
    rand_game_2 = rand_games[1]
    rand_game_3 = rand_games[2]

    return render_template(
        "reviews.html", game_reviews=pagination_game_reviews,
        pagination=pagination, rand_game_1=rand_game_1,
        rand_game_2=rand_game_2, rand_game_3=rand_game_3,
        reviewData=reviewData, navGameData=navGameData)


# =======================
# Reviews - XBOX Platform
# =======================

@app.route("/community-reviews/xbox")
def reviews_xbox():
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    # Grab review data for autocomplete function
    reviewData = mongo.db.user_reviews.find({}).distinct("game_title")

    # Find reviews with xbox platform
    game_reviews = mongo.db.user_reviews.find({"platform": "xbox"})

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

    # Set carousel images
    random_games = mongo.db.all_pc_games.aggregate([
        {"$match": {"favourite": True}},
        {"$sample": {"size": 3}}
    ])

    rand_games = []
    for game in random_games:
        rand_games.append(game)

    rand_game_1 = rand_games[0]
    rand_game_2 = rand_games[1]
    rand_game_3 = rand_games[2]

    return render_template(
        "reviews.html", game_reviews=pagination_game_reviews,
        pagination=pagination, rand_game_1=rand_game_1,
        rand_game_2=rand_game_2, rand_game_3=rand_game_3,
        reviewData=reviewData, navGameData=navGameData)


# ==============================
# Reviews - Playstation Platform
# ==============================

@app.route("/community-reviews/playstation")
def reviews_playstation():
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    # Grab review data for autocomplete function
    reviewData = mongo.db.user_reviews.find({}).distinct("game_title")

    # Find reviews with playstation platform
    game_reviews = mongo.db.user_reviews.find({"platform": "playstation"})

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

    # Set carousel images
    random_games = mongo.db.all_pc_games.aggregate([
        {"$match": {"favourite": True}},
        {"$sample": {"size": 3}}
    ])

    rand_games = []
    for game in random_games:
        rand_games.append(game)

    rand_game_1 = rand_games[0]
    rand_game_2 = rand_games[1]
    rand_game_3 = rand_games[2]

    return render_template(
        "reviews.html", game_reviews=pagination_game_reviews,
        pagination=pagination, rand_game_1=rand_game_1,
        rand_game_2=rand_game_2, rand_game_3=rand_game_3,
        reviewData=reviewData, navGameData=navGameData)


# ===========================
# Reviews - Nintendo Platform
# ===========================

@app.route("/community-reviews/nintendo")
def reviews_nintendo():
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    # Grab review data for autocomplete function
    reviewData = mongo.db.user_reviews.find({}).distinct("game_title")

    # Find reviews with nintendo platform
    game_reviews = mongo.db.user_reviews.find({"platform": "nintendo"})

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

    # Set carousel images
    random_games = mongo.db.all_pc_games.aggregate([
        {"$match": {"favourite": True}},
        {"$sample": {"size": 3}}
    ])

    rand_games = []
    for game in random_games:
        rand_games.append(game)

    rand_game_1 = rand_games[0]
    rand_game_2 = rand_games[1]
    rand_game_3 = rand_games[2]

    return render_template(
        "reviews.html", game_reviews=pagination_game_reviews,
        pagination=pagination, rand_game_1=rand_game_1,
        rand_game_2=rand_game_2, rand_game_3=rand_game_3,
        reviewData=reviewData, navGameData=navGameData)


# ======================
# Profile - User Reviews
# ======================

@app.route("/profile/<username>/reviews")
def profile_reviews(username):
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    reviews = mongo.db.user_reviews.find({})
    user = mongo.db.users.find_one({"username": session["user"]})
    return render_template(
        "profile-reviews.html", username=session["user"],
        reviews=reviews, user=user, navGameData=navGameData)


# =============
# Submit Review
# =============

@app.route("/submit-review", methods=["GET", "POST"])
def submit_review():
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    if request.method == "POST":
        # Find game data for displaying game review
        title = request.form.get("query")
        game = mongo.db.all_pc_games.find_one({"game_title": title})
        img_full = game["game_img_full"]

        display_name = mongo.db.users.find_one(
            {"username": session["user"]})["display_name"]

        # Set current date
        date = datetime.datetime.now()

        review = {
            "game_title": title,
            "game_img_full": img_full,
            "platform": request.form.get("platform-select").lower(),
            "summary": request.form.get("summary"),
            "gameplay_rating": int(request.form.get("gameplay-stars")),
            "gameplay": request.form.get("gameplay"),
            "visuals_rating": int(request.form.get("visuals-stars")),
            "visuals": request.form.get("visuals"),
            "sound_rating": int(request.form.get("sound-stars")),
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

    # Grab review data for autocomplete function
    gameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    return render_template(
        "reviews-review_form.html", navGameData=navGameData,
        gameData=gameData)


# ======================
# Profile- Submit Review
# ======================

@app.route("/submit-review/<game_id>", methods=["GET", "POST"])
def profile_submit_review(game_id):
    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    if request.method == "POST":

        # Find game data for displaying game review
        title = request.form.get("query")
        game = mongo.db.all_pc_games.find_one({"game_title": title})
        img_full = game["game_img_full"]

        # Set current date
        date = datetime.datetime.now()

        display_name = mongo.db.users.find_one(
            {"username": session["user"]})["display_name"]

        review = {
            "game_title": title,
            "game_img_full": img_full,
            "platform": request.form.get("platform-select").lower(),
            "summary": request.form.get("summary"),
            "gameplay_rating": int(request.form.get("gameplay-stars")),
            "gameplay": request.form.get("gameplay"),
            "visuals_rating": int(request.form.get("visuals-stars")),
            "visuals": request.form.get("visuals"),
            "sound_rating": int(request.form.get("sound-stars")),
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

    # Grab review data for autocomplete function
    gameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    return render_template(
        "profile-review_form.html", matching_results=games, game=game,
        username=session["user"], navGameData=navGameData,
        gameData=gameData)


# =====================
# Profile - Edit Review
# =====================

@app.route("/edit-review/<game_id>", methods=["GET", "POST"])
def edit_review(game_id):
    # Find game to assign to review form
    game = mongo.db.user_games.find_one({"_id": (ObjectId(game_id))})

    game_title = game["game_title"]
    img_full = game["game_img_full"]

    review = mongo.db.user_reviews.find_one(
            {"$and": [{"username": session["user"]},
                      {"game_title": game_title}]})

    review_id = review["_id"]
    submission_date = review["date_submitted"]

    display_name = mongo.db.users.find_one(
        {"username": session["user"]})["display_name"]

    if request.method == "POST":
        date = datetime.datetime.now()

        update = {
            "game_title": game_title,
            "game_img_full": img_full,
            "platform": request.form.get("platform-select").lower(),
            "summary": request.form.get("summary"),
            "gameplay_rating": int(request.form.get("gameplay-stars")),
            "gameplay": request.form.get("gameplay"),
            "visuals_rating": int(request.form.get("visuals-stars")),
            "visuals": request.form.get("visuals"),
            "sound_rating": int(request.form.get("sound-stars")),
            "sound": request.form.get("sound"),
            "recommended": request.form.get("radioRecommend"),
            "date_submitted": submission_date,
            "last_updated": date.strftime("%x"),
            "username": session["user"],
            "display_name": display_name
        }
        mongo.db.user_reviews.update({"_id": review_id}, update)
        flash("Review Successfully Updated")
        return redirect(url_for('reviews'))

    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    return render_template(
        "reviews-edit_review.html", game=game, review=review,
        navGameData=navGameData)


# =============================
# Profile Reviews - Edit Review
# =============================

@app.route("/profile/edit-review/<review_id>", methods=["GET", "POST"])
def profile_edit_review(review_id):
    # Find game to assign to review form
    review = mongo.db.user_reviews.find_one({"_id": ObjectId(review_id)})

    game_title = review["game_title"]
    img_full = review["game_img_full"]
    submission_date = review["date_submitted"]

    display_name = mongo.db.users.find_one(
        {"username": session["user"]})["display_name"]

    if request.method == "POST":
        date = datetime.datetime.now()

        update = {
            "game_title": game_title,
            "game_img_full": img_full,
            "platform": request.form.get("platform-select").lower(),
            "summary": request.form.get("summary"),
            "gameplay_rating": int(request.form.get("gameplay-stars")),
            "gameplay": request.form.get("gameplay"),
            "visuals_rating": int(request.form.get("visuals-stars")),
            "visuals": request.form.get("visuals"),
            "sound_rating": int(request.form.get("sound-stars")),
            "sound": request.form.get("sound"),
            "recommended": request.form.get("radioRecommend"),
            "date_submitted": submission_date,
            "last_updated": date.strftime("%x"),
            "username": session["user"],
            "display_name": display_name
        }
        mongo.db.user_reviews.update({"_id": ObjectId(review_id)}, update)
        flash("Review Successfully Updated")
        return redirect(url_for('reviews'))

    # Grab game data for autocomplete function in navbar
    navGameData = mongo.db.all_pc_games.find({}).distinct("game_title")

    return render_template(
        "profile-edit_review.html", review=review, navGameData=navGameData)


# ======================
# Profile- Delete Review
# ======================

@app.route("/delete-review/<review_id>")
def delete_review(review_id):
    # Find review and remove it from db
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
