import os
from flask import Flask
from flask_pymongo import PyMongo
from scrape_steamstore import steam_bestsellers, steam_award_winners
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


# ----------------------------------------------------------------- BESTSELLERS

# ------------------------------ Steam bestsellers - lists

bs_game_index = []
bs_game_title = []
bs_game_tags = []
bs_game_img_sm = []
bs_platform_pc = []
bs_game_link = []

# ------------------------------ Steam award winners - lists

award_index = []
award_year = []
award_title = []
award_winner = []
award_winner_img = []

# ------------------------------ Get data from Steam Store dicitionary


def get__bestseller_dict():
    for k, v in steam_bestsellers.items():
        bs_game_index.append(k)

    for k, v in steam_bestsellers.items():
        for k1, v1 in v.items():
            if k1 == "title":
                bs_game_title.append(v1)
            if k1 == "tags":
                bs_game_tags.append(v1)
            if k1 == "image":
                bs_game_img_sm.append(v1)
            if k1 == "pc_platform_tags":
                bs_platform_pc.append(v1)
            if k1 == "game_link":
                bs_game_link.append(v1)


# ------------------------------ Add data to database

def add_bestsellers_to_db():
    for i in range(len(bs_game_title)):
        bestseller = {
            "game_index": bs_game_index[i],
            "game_title": bs_game_title[i],
            "game_top_tags": bs_game_tags[i],
            "game_img_sm": bs_game_img_sm[i],
            "platform_tags_pc": bs_platform_pc[i],
            "game_link": bs_game_link[i]
        }
        # Stop data from being re-added if it already exists
        existing_data = mongo.db.steam_bestsellers.find_one(
            {"game_title": bs_game_title[i]}
        )
        if not existing_data:
            mongo.db.steam_bestsellers.insert_one(bestseller)


# ------------------------------ Update data in database

def update_bestsellers_db():
    for i in range(len(bs_game_title)):
        bestseller = {
            "game_index": bs_game_index[i],
            "game_title": bs_game_title[i],
            "game_top_tags": bs_game_tags[i],
            "game_img_sm": bs_game_img_sm[i],
            "platform_tags_pc": bs_platform_pc[i],
            "game_link": bs_game_link[i]
        }

        # Stop data from being re-added if it already exists
        existing_data = mongo.db.steam_bestsellers.find_one(
            {"game_title": bs_game_title[i]}
        )
        if not existing_data:
            mongo.db.steam_bestsellers.insert_one(bestseller)


# ------------------------------ Remove all data from database

def remove_bestsellers_db_data():
    mongo.db.steam_bestsellers.remove({})


# --------------------------------------------------------------- AWARD WINNERS

# ------------------------------ Get data from Steam Awards dicitionary

def get_awardwinners_dict():
    for k, v in steam_award_winners.items():
        award_index.append(k)

    for k, v in steam_award_winners.items():
        for k1, v1 in v.items():
            if k1 == "year":
                award_year.append(v1)
            if k1 == "award":
                award_title.append(v1)
            if k1 == "winner":
                award_winner.append(v1)
            if k1 == "img":
                award_winner_img.append(v1)


# ------------------------------ Add data to database

def add_awardwinners_to_db():
    for i in range(len(award_winner)):
        winner = {
            "game_index": award_index[i],
            "award_year": award_year[i],
            "award_title": award_title[i],
            "winner": award_winner[i],
            "winner_img": award_winner_img[i]
        }
        # Stop data from being re-added if it already exists
        existing_data = mongo.db.steam_bestsellers.find_one(
            {"winner": award_winner[i]}
        )
        if not existing_data:
            mongo.db.steam_awardwinners.insert_one(winner)


# ------------------ Call dictionary functions

get__bestseller_dict()
add_bestsellers_to_db()
update_bestsellers_db()
remove_bestsellers_db_data()

get_awardwinners_dict()
add_awardwinners_to_db()
