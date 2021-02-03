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


get_dict_items()
