import os
from flask import Flask
from flask_pymongo import PyMongo
from scrape_steamstore import steam_bestsellers
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


# ------------------------------ Steam Store data - lists

game_index = []
game_title = []
game_tags = []
game_img_sm = []
platform_pc = []
game_link = []

# ------------------------------ Get data from Steam Store dicitionary


def get_dict_items():
    for k, v in steam_bestsellers.items():
        game_index.append(k)

    for k, v in steam_bestsellers.items():
        for k1, v1 in v.items():
            if k1 == "title":
                game_title.append(v1)
            if k1 == "tags":
                game_tags.append(v1)
            if k1 == "image":
                game_img_sm.append(v1)
            if k1 == "pc_platform_tags":
                platform_pc.append(v1)
            if k1 == "game_link":
                game_link.append(v1)


# ------------------------------ Add data to database

def add_to_db():
    for i in range(len(game_title)):
        bestseller = {
            "game_index": game_index[i],
            "game_title": game_title[i],
            "game_top_tags": game_tags[i],
            "game_img_sm": game_img_sm[i],
            "platform_tags_pc": platform_pc[i],
            "game_link": game_link[i]
        }
        # Stop data from being re-added if it already exists
        existing_data = mongo.db.steam_bestsellers.find_one(
            {"game_title": game_title[i]}
        )
        if not existing_data:
            mongo.db.steam_bestsellers.insert_one(bestseller)


# ------------------------------ Update data in database

def update_db():
    for i in range(len(game_title)):
        bestseller = {
            "game_index": game_index[i],
            "game_title": game_title[i],
            "game_top_tags": game_tags[i],
            "game_img_sm": game_img_sm[i],
            "platform_tags_pc": platform_pc[i],
            "game_link": game_link[i]
        }

        mongo.db.steam_bestsellers.update(
            {"game_index": game_index[i]}, bestseller)


# ------------------------------ Remove all data from database

def remove_db_data():
    mongo.db.steam_bestsellers.remove({})


get_dict_items()
update_db()
add_to_db()
remove_db_data()

