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


# --------------------------------------------------------------- AWARD WINNERS

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


# --------------------------------------------------------------- ACTION GAMES

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


# ------------------------------------------------------------- ADVENTURE GAMES

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



# --------------------------------------------------------------- RPG GAMES

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


# -------------------------------------------------------------- STRATEGY GAMES

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


# ----------------------------------------------------------- MULTIPLAYER GAMES

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


# ------------------ Call dictionary functions

get_bestseller_dict()
get_awardwinners_dict()
get_action_games_dict()
get_adventure_games_dict()
get_RPG_games_dict()
get_strategy_games_dict()
get_multiplayer_games_dict()
