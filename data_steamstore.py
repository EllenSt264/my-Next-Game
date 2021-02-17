import os
from flask import Flask
from flask_pymongo import PyMongo
from scrape_steamstore import (
    steam_bestsellers, steam_award_winners, steam_action_games,
    steam_adventure_games, steam_RPG_games,
    steam_strategy_games, steam_multiplayer_games,
    pc_games)
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


# ------------------------------ Steam bestsellers - lists

bs_game_index = []
bs_game_title = []
bs_game_tags = []
bs_game_img_sm = []
bs_game_img_full = []
bs_platform_pc = []
bs_game_link = []

# ------------------------------ Steam award winners - lists

award_index = []
award_year = []
award_title = []
award_winner = []
award_winner_img = []

# ------------------------------ Steam games - lists

# --- Action games

action_game_index = []
action_game_title = []
action_game_tags = []
action_game_img_sm = []
action_game_img_full = []
action_platform_pc = []
action_game_link = []

# --- Adventure games

adventure_game_index = []
adventure_game_title = []
adventure_game_tags = []
adventure_game_img_sm = []
adventure_game_img_full = []
adventure_platform_pc = []
adventure_game_link = []

# --- RPG games

RPG_game_index = []
RPG_game_title = []
RPG_game_tags = []
RPG_game_img_sm = []
RPG_game_img_full = []
RPG_platform_pc = []
RPG_game_link = []

# --- Strategy games

strategy_game_index = []
strategy_game_title = []
strategy_game_tags = []
strategy_game_img_sm = []
strategy_game_img_full = []
strategy_platform_pc = []
strategy_game_link = []

# --- Multiplayer games

multiplayer_game_index = []
multiplayer_game_title = []
multiplayer_game_tags = []
multiplayer_game_img_sm = []
multiplayer_game_img_full = []
multiplayer_platform_pc = []
multiplayer_game_link = []

# --- PC games

pc_game_index = []
pc_game_title = []
pc_game_tags = []
pc_game_img_sm = []
pc_game_img_full = []
pc_platform_pc = []
pc_game_link = []


# ----------------------------------------------------------------- BESTSELLERS

# ------------------------------ Get data from Steam Store dicitionary


def get_bestseller_dict():
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
            if k1 == "full_image":
                bs_game_img_full.append(v1)
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
            "game_img_full": bs_game_img_full[i],
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
        existing_data = mongo.db.steam_awardwinners.find_one(
            {"winner": award_winner[i]}
        )
        if not existing_data:
            mongo.db.steam_awardwinners.insert_one(winner)


# --------------------------------------------------------------- ACTION GAMES

# ------------------------------ Get data from Steam Store dicitionary

def get_action_games_dict():
    for k, v in steam_action_games.items():
        action_game_index.append(k)

    for k, v in steam_action_games.items():
        for k1, v1 in v.items():
            if k1 == "title":
                action_game_title.append(v1)
            if k1 == "tags":
                action_game_tags.append(v1)
            if k1 == "image":
                action_game_img_sm.append(v1)
            if k1 == "full_image":
                action_game_img_full.append(v1)
            if k1 == "pc_platform_tags":
                action_platform_pc.append(v1)
            if k1 == "game_link":
                action_game_link.append(v1)


# ------------------------------ Add data to database

def add_action_games_to_db():
    for i in range(len(action_game_title)):
        game = {
            "game_index": action_game_index[i],
            "game_title": action_game_title[i], 
            "game_top_tags": action_game_tags[i],
            "game_img_sm": action_game_img_sm[i],
            "game_img_full": action_game_img_full[i],
            "platform_tags_pc": action_platform_pc[i],
            "game_link": action_game_link[i]
        }
        # Stop data from being re-added if it already exists
        existing_data = mongo.db.steam_action_games.find_one(
            {"game_title": action_game_title[i]}
        )
        if not existing_data:
            mongo.db.steam_action_games.insert_one(game)


# ------------------------------------------------------------- ADVENTURE GAMES

# ------------------------------ Get data from Steam Store dicitionary

def get_adventure_games_dict():
    for k, v in steam_adventure_games.items():
        adventure_game_index.append(k)

    for k, v in steam_adventure_games.items():
        for k1, v1 in v.items():
            if k1 == "title":
                adventure_game_title.append(v1)
            if k1 == "tags":
                adventure_game_tags.append(v1)
            if k1 == "image":
                adventure_game_img_sm.append(v1)
            if k1 == "full_image":
                adventure_game_img_full.append(v1)
            if k1 == "pc_platform_tags":
                adventure_platform_pc.append(v1)
            if k1 == "game_link":
                adventure_game_link.append(v1)


# ------------------------------ Add data to database

def add_adventure_games_to_db():
    for i in range(len(adventure_game_title)):
        game = {
            "game_index": adventure_game_index[i],
            "game_title": adventure_game_title[i],
            "game_top_tags": adventure_game_tags[i],
            "game_img_sm": adventure_game_img_sm[i],
            "game_img_full": adventure_game_img_full[i],
            "platform_tags_pc": adventure_platform_pc[i],
            "game_link": adventure_game_link[i]
        }
        # Stop data from being re-added if it already exists
        existing_data = mongo.db.steam_adventure_games.find_one(
            {"game_title": adventure_game_title[i]}
        )
        if not existing_data:
            mongo.db.steam_adventure_games.insert_one(game)


# --------------------------------------------------------------- RPG GAMES

# ------------------------------ Get data from Steam Store dicitionary


def get_RPG_games_dict():
    for k, v in steam_RPG_games.items():
        RPG_game_index.append(k)

    for k, v in steam_RPG_games.items():
        for k1, v1 in v.items():
            if k1 == "title":
                RPG_game_title.append(v1)
            if k1 == "tags":
                RPG_game_tags.append(v1)
            if k1 == "image":
                RPG_game_img_sm.append(v1)
            if k1 == "full_image":
               RPG_game_img_full.append(v1)
            if k1 == "pc_platform_tags":
                RPG_platform_pc.append(v1)
            if k1 == "game_link":
                RPG_game_link.append(v1)


# ------------------------------ Add data to database

def add_RPG_games_to_db():
    for i in range(len(RPG_game_title)):
        game = {
            "game_index": RPG_game_index[i],
            "game_title": RPG_game_title[i],
            "game_top_tags": RPG_game_tags[i],
            "game_img_sm": RPG_game_img_sm[i],
            "game_img_full": RPG_game_img_full[i],
            "platform_tags_pc": RPG_platform_pc[i],
            "game_link": RPG_game_link[i]
        }
        # Stop data from being re-added if it already exists
        existing_data = mongo.db.steam_RPG_games.find_one(
            {"game_title": RPG_game_title[i]}
        )
        if not existing_data:
            mongo.db.steam_RPG_games.insert_one(game)


# -------------------------------------------------------------- STRATEGY GAMES

# ------------------------------ Get data from Steam Store dicitionary


def get_strategy_games_dict():
    for k, v in steam_strategy_games.items():
        strategy_game_index.append(k)

    for k, v in steam_strategy_games.items():
        for k1, v1 in v.items():
            if k1 == "title":
                strategy_game_title.append(v1)
            if k1 == "tags":
                strategy_game_tags.append(v1)
            if k1 == "image":
                strategy_game_img_sm.append(v1)
            if k1 == "full_image":
                strategy_game_img_full.append(v1)
            if k1 == "pc_platform_tags":
                strategy_platform_pc.append(v1)
            if k1 == "game_link":
                strategy_game_link.append(v1)


# ------------------------------ Add data to database

def add_strategy_games_to_db():
    for i in range(len(strategy_game_title)):
        game = {
            "game_index": strategy_game_index[i],
            "game_title": strategy_game_title[i],
            "game_top_tags": strategy_game_tags[i],
            "game_img_sm": strategy_game_img_sm[i],
            "game_img_full": strategy_game_img_full[i],
            "platform_tags_pc": strategy_platform_pc[i],
            "game_link": strategy_game_link[i]
        }
        # Stop data from being re-added if it already exists
        existing_data = mongo.db.steam_strategy_games.find_one(
            {"game_title": strategy_game_title[i]}
        )
        if not existing_data:
            mongo.db.steam_strategy_games.insert_one(game)


# ----------------------------------------------------------- MULTIPLAYER GAMES

# ------------------------------ Get data from Steam Store dicitionary


def get_multiplayer_games_dict():
    for k, v in steam_multiplayer_games.items():
        multiplayer_game_index.append(k)

    for k, v in steam_multiplayer_games.items():
        for k1, v1 in v.items():
            if k1 == "title":
                multiplayer_game_title.append(v1)
            if k1 == "tags":
                multiplayer_game_tags.append(v1)
            if k1 == "image":
                multiplayer_game_img_sm.append(v1)
            if k1 == "full_image":
                multiplayer_game_img_full.append(v1)
            if k1 == "pc_platform_tags":
                multiplayer_platform_pc.append(v1)
            if k1 == "game_link":
                multiplayer_game_link.append(v1)


# ------------------------------ Add data to database

def add_multiplayer_games_to_db():
    for i in range(len(multiplayer_game_title)):
        game = {
            "game_index": multiplayer_game_index[i],
            "game_title": multiplayer_game_title[i],
            "game_top_tags": multiplayer_game_tags[i],
            "game_img_sm": multiplayer_game_img_sm[i],
            "game_img_full": multiplayer_game_img_full[i],
            "platform_tags_pc": multiplayer_platform_pc[i],
            "game_link": multiplayer_game_link[i]
        }
        # Stop data from being re-added if it already exists
        existing_data = mongo.db.steam_multiplayer_games.find_one(
            {"game_title": multiplayer_game_title[i]}
        )
        if not existing_data:
            mongo.db.steam_multiplayer_games.insert_one(game)


# ----------------------------------------------------------- ALL PC GAMES


def get_pc_games():
    for k, v in pc_games.items():
        pc_game_index.append(k)

        for k1, v1 in v.items():
            if k1 == "title":
                pc_game_title.append(v1)
            if k1 == "tags":
                pc_game_tags.append(v1)
            if k1 == "image":
                pc_game_img_sm.append(v1)
            if k1 == "full_image":
                pc_game_img_full.append(v1)
            if k1 == "pc_platform_tags":
                pc_platform_pc.append(v1)
            if k1 == "game_link":
                pc_game_link.append(v1)


def add_pc_games_to_db():
    for i in range(len(pc_game_title)):
        game = {
            "game_index": pc_game_index[i],
            "game_title": pc_game_title[i],
            "game_top_tags": pc_game_tags[i],
            "game_img_sm": pc_game_img_sm[i],
            "game_img_full": pc_game_img_full[i],
            "platform_tags_pc": pc_platform_pc[i],
            "game_link": pc_game_link[i]
        }
        # Stop data from being re-added if it already exists
        existing_data = mongo.db.pc_games.find_one(
            {"game_title": pc_game_title[i]}
        )
        if not existing_data:
            mongo.db.pc_games.insert_one(game)

# ------------------ Call dictionary functions


# Bestsellers
get_bestseller_dict()
add_bestsellers_to_db()
update_bestsellers_db()
remove_bestsellers_db_data()

# Award Winners
get_awardwinners_dict()
add_awardwinners_to_db()

# Action games
get_action_games_dict()
add_action_games_to_db()

# Adventure games
get_adventure_games_dict()
add_adventure_games_to_db()

# RPG games
get_RPG_games_dict()
add_RPG_games_to_db()

# Strategy games
get_strategy_games_dict()
add_strategy_games_to_db()

# Multiplayer games
get_multiplayer_games_dict()
add_multiplayer_games_to_db()

# PC games
get_pc_games()
add_pc_games_to_db()
