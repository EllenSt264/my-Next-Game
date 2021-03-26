import os
from flask import Flask
from flask_pymongo import PyMongo
from scrape_steamstore import (
    steam_bestsellers, steam_award_winners, steam_action_games,
    steam_adventure_games, steam_RPG_games,
    steam_strategy_games, steam_multiplayer_games, favourites)
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
award_game_tags = []
award_platform_pc = []
award_game_link = []

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

# --- Game favourites

favourite_links = []
favourites_game_title = []
favourites_game_img = []
favourites_game_screenshots = []
favourites_game_tags = []
favourites_platform_pc = []
favourite_game_summary = []


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
        for k1, v1 in v.items():
            if k1 == "year":
                award_year.append(v1)
            if k1 == "award":
                award_title.append(v1)
            if k1 == "winner":
                award_winner.append(v1)
            if k1 == "img":
                award_winner_img.append(v1)
            if k1 == "tags":
                award_game_tags.append(v1)
            if k1 == "pc_platform_tags":
                award_platform_pc.append(v1)
            if k1 == "game_link":
                award_game_link.append(v1)


# --------------------------------------------------------------- ACTION GAMES

def get_action_games_dict():
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


# ----------------------------------------------------------- GAME FAVOURITES

def get_favourites_games_dict():
    for k, v in favourites.items():
        for k1, v1 in v.items():
            if k1 == "title":
                favourites_game_title.append(v1)
            if k1 == "tags":
                favourites_game_tags.append(v1)
            if k1 == "image":
                favourites_game_img.append(v1)
            if k1 == "screenshots":
                favourites_game_screenshots.append(v1)
            if k1 == "pc_platform_tags":
                favourites_platform_pc.append(v1)
            if k1 == "game_link":
                favourite_links.append(v1)
            if k1 == "game_summary":
                favourite_game_summary.append(v1)


# ------------------ Call dictionary functions

get_bestseller_dict()
get_awardwinners_dict()
get_action_games_dict()
get_adventure_games_dict()
get_RPG_games_dict()
get_strategy_games_dict()
get_multiplayer_games_dict()
get_favourites_games_dict()


# ----------------------------------------------------------- ADD TO DATABASE


def add_to_db():
    # ---------------------------------------- Bestseller
    for i in range(len(bs_game_title)):
        bestseller = {
            "game_title": bs_game_title[i],
            "game_top_tags": bs_game_tags[i],
            "game_img_full": bs_game_img_full[i],
            "platform_tags_pc": bs_platform_pc[i],
            "game_link": bs_game_link[i],
            "liked_by": None,
            "likes": 0,
            "bestseller": True
        }
        # Check game title already exists in db
        existing_bestseller_title = mongo.db.all_pc_games.find_one(
            {"game_title": bs_game_title[i]})

        # Update rather than replace or duplicate the existing game
        if existing_bestseller_title:
            bestseller_id = existing_bestseller_title["_id"]
            mongo.db.all_pc_games.update_one(
                {"_id": bestseller_id}, {"$set": {"bestseller": True}})
        # Otherwise, add new document to db
        else:
            mongo.db.all_pc_games.insert_one(bestseller)

    # ---------------------------------------- Award winners
    for i in range(len(award_title)):
        awardwinner = {
            "game_title": award_winner[i],
            "game_img_full": award_winner_img[i],
            "game_top_tags": award_game_tags[i],
            "platform_tags_pc": award_platform_pc[i],
            "game_link": award_game_link[i],
            "award_year": award_year[i],
            "award_title": award_title[i],
            "liked_by": None,
            "likes": 0,
            "awardwinner": True
        }
        # Check game title already exists in db
        existing_awardwinner_title = mongo.db.all_pc_games.find_one(
            {"game_title": award_winner[i]})

        # Update rather than replace or duplicate the existing game
        if existing_awardwinner_title:
            awardwinner_id = existing_awardwinner_title["_id"]
            # If the game has multiple awards that need to be added
            if existing_awardwinner_title["awardwinner"]:
                mongo.db.all_pc_games.update_one(
                    {"_id": awardwinner_id},
                    {"$set": {"award_title_2": award_title[i]}})
            else:
                mongo.db.all_pc_games.update_one(
                    {"_id": awardwinner_id},
                    {"$set": {
                        "award_year": award_year[i],
                        "award_title": award_title[i],
                        "awardwinner": True
                    }})
        # Otherwise, add new document to db
        else:
            mongo.db.all_pc_games.insert_one(awardwinner)

    # ---------------------------------------- Action
    for i in range(len(action_game_title)):
        action = {
            "game_title": action_game_title[i],
            "game_top_tags": action_game_tags[i],
            "game_img_full": action_game_img_full[i],
            "platform_tags_pc": action_platform_pc[i],
            "game_link": action_game_link[i],
            "liked_by": None,
            "likes": 0,
            "action": True
        }
        # Check game title already exists in db
        existing_action_title = mongo.db.all_pc_games.find_one(
            {"game_title": action_game_title[i]})

        # Update rather than replace or duplicate the existing game
        if existing_action_title:
            action_id = existing_action_title["_id"]
            mongo.db.all_pc_games.update_one(
                {"_id": action_id}, {"$set": {"action": True}})
        # Otherwise, add new document to db
        else:
            mongo.db.all_pc_games.insert_one(action)

    # ---------------------------------------- Adventure
    for i in range(len(adventure_game_title)):
        adventure = {
            "game_title": adventure_game_title[i],
            "game_top_tags": adventure_game_tags[i],
            "game_img_full": adventure_game_img_full[i],
            "platform_tags_pc": adventure_platform_pc[i],
            "game_link": adventure_game_link[i],
            "liked_by": None,
            "likes": 0,
            "adventure": True
        }
        # Check game title already exists in db
        existing_adventure_title = mongo.db.all_pc_games.find_one(
            {"game_title": adventure_game_title[i]})

        # Update rather than replace or duplicate the existing game
        if existing_adventure_title:
            adventure_id = existing_adventure_title["_id"]
            mongo.db.all_pc_games.update_one(
                {"_id": adventure_id}, {"$set": {"adventure": True}})
        # Otherwise, add new document to db
        else:
            mongo.db.all_pc_games.insert_one(adventure)

    # ---------------------------------------- RPG
    for i in range(len(RPG_game_title)):
        RPG = {
            "game_title": RPG_game_title[i],
            "game_top_tags": RPG_game_tags[i],
            "game_img_full": RPG_game_img_full[i],
            "platform_tags_pc": RPG_platform_pc[i],
            "game_link": RPG_game_link[i],
            "liked_by": None,
            "likes": 0,
            "RPG": True
        }
        # Check game title already exists in db
        existing_RPG_title = mongo.db.all_pc_games.find_one(
            {"game_title": RPG_game_title[i]})

        # Update rather than replace or duplicate the existing game
        if existing_RPG_title:
            RPG_id = existing_RPG_title["_id"]
            mongo.db.all_pc_games.update_one(
                {"_id": RPG_id}, {"$set": {"RPG": True}})
        # Otherwise, add new document to db
        else:
            mongo.db.all_pc_games.insert_one(RPG)

    # ---------------------------------------- Strategy
    for i in range(len(strategy_game_title)):
        strategy = {
            "game_title": strategy_game_title[i],
            "game_top_tags": strategy_game_tags[i],
            "game_img_full": strategy_game_img_full[i],
            "platform_tags_pc": strategy_platform_pc[i],
            "game_link": strategy_game_link[i],
            "liked_by": None,
            "likes": 0,
            "strategy": True
        }
        # Check game title already exists in db
        existing_strategy_title = mongo.db.all_pc_games.find_one(
            {"game_title": strategy_game_title[i]})

        # Update rather than replace or duplicate the existing game
        if existing_strategy_title:
            strategy_id = existing_strategy_title["_id"]
            mongo.db.all_pc_games.update_one(
                {"_id": strategy_id}, {"$set": {"strategy": True}})
        # Otherwise, add new document to db
        else:
            mongo.db.all_pc_games.insert_one(strategy)

    # ---------------------------------------- Multiplayer
    for i in range(len(multiplayer_game_title)):
        multiplayer = {
            "game_title": multiplayer_game_title[i],
            "game_top_tags": multiplayer_game_tags[i],
            "game_img_full": multiplayer_game_img_full[i],
            "platform_tags_pc": multiplayer_platform_pc[i],
            "game_link": multiplayer_game_link[i],
            "liked_by": None,
            "likes": 0,
            "multiplayer": True
        }
        # Check game title already exists in db
        existing_multiplayer_title = mongo.db.all_pc_games.find_one(
            {"game_title": multiplayer_game_title[i]})

        # Update rather than replace or duplicate the existing game
        if existing_multiplayer_title:
            multiplayer_id = existing_multiplayer_title["_id"]
            mongo.db.all_pc_games.update_one(
                {"_id": multiplayer_id}, {"$set": {"multiplayer": True}})
        # Otherwise, add new document to db
        else:
            mongo.db.all_pc_games.insert_one(multiplayer)

    # ---------------------------------------- Favourites
    for i in range(len(favourites_game_title)):
        favourite = {
            "game_title": favourites_game_title[i],
            "game_top_tags": favourites_game_tags[i],
            "game_img_full": favourites_game_img[i],
            "platform_tags_pc": favourites_platform_pc[i],
            "game_link": favourite_links[i],
            "screenshots": favourites_game_screenshots,
            "game_summary": favourite_game_summary,
            "liked_by": None,
            "likes": 0,
            "favourite": True
        }
        # Check game title already exists in db
        existing_favourites_title = mongo.db.all_pc_games.find_one(
            {"game_title": favourites_game_title[i]})

        # Update rather than replace or duplicate the existing game
        if existing_favourites_title:
            favourites_id = existing_favourites_title["_id"]
            mongo.db.all_pc_games.update_one(
                    {"_id": favourites_id},
                    {"$set": {
                        "screenshots": favourites_game_screenshots[i],
                        "game_summary": favourite_game_summary[i],
                        "favourite": True
                    }})
        # Otherwise, add new document to db
        else:
            mongo.db.all_pc_games.insert_one(favourite)


add_to_db()
