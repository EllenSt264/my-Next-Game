import os
import re
import requests
from bs4 import BeautifulSoup
from flask import Flask
from flask_pymongo import PyMongo
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


# -------------- Lists

links = []
categories = []

game_title = []
game_img = []
game_screenshots = []
game_tags = []
game_platform_tags = []
game_summary = []


# -------------- Dictionary

custom_games = {}


# ---------------------------------------------------------- GRAB LINKS FROM DB

def grab_links():
    db = mongo.db.game_queue.find()

    for i in db:
        links.append(i["game_link"])
        categories.append(i["category"])


# ----------------------------------------------------------------- SCRAPE DATA

def scrape_data():
    url_list = links

    for url in url_list:

        cookies = {"birthtime": "786240001", "lastagecheckage": "1-0-1995"}
        source = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(source.text, "html.parser")

        # ------------------------------ Game title
        for item in soup.select(".page_title_area.game_title_area"):
            for title in item.select(".apphub_AppName"):
                game_title.append(title.text)

        # ------------------------------ Game image

        for item in soup.select(".page_content_ctn"):
            if item.find("img", {"class": "package_header"}):
                img = item.select(".package_header")
                for i in img:
                    game_img.append(i["src"])

            else:
                img = item.select(".game_header_image_full")
                for i in img:
                    game_img.append(i["src"])

        # ------------------------------ Game image - screenshots

        screenshots = []

        for item in soup.select(".highlight_player_item.highlight_screenshot"):
            for i in item.select(".screenshot_holder"):
                images = i.select(".highlight_screenshot_link", href=True)
                for img in images:
                    screenshots.append(img.attrs["href"])

        game_screenshots.append(screenshots)

        # ------------------------------ Game genre tags

        tags_inner = []

        for item in soup.select(".glance_tags.popular_tags"):
            for a in item.select("a", href=True, limit=5):
                tag = a.text.strip()
                tags_inner.append(tag)

        game_tags.append(tags_inner)

        # ------------------------------ Game platform tags

        for item in soup.select(".game_area_purchase_platform"):
            pc_platforms = item.select(".platform_img")

            platforms = str(pc_platforms)

            platforms = platforms.replace(
                '<span class="platform_img win"></span>', 'win'
            ).replace(
                '<span class="platform_img mac"></span>', 'mac'
            ).replace(
                '<span class="platform_img linux"></span>', 'linux'
            ).replace(
                '[', ''
            ).replace(
                ']', ''
            )

            platform_lis = list(platforms.split(","))
            game_platform_tags.append(platform_lis)

        # ------------------------------ Game summary

        for item in soup.select("#game_area_description"):
            res = item.text

            regex = re.compile(r"[\n\r\t]")
            text = regex.sub(" ", res)

            summary = []

            sentences = text.split(".")

            for i in sentences:
                summary.append(i)

            shortended = summary[:4]
            summary_str = ".".join(shortended)
            summary_str = summary_str.replace("About This Game ", "").replace(
                "Game: ", "").replace("         ", "").replace("   ", " ")

            game_summary.append(summary_str)


# --------------------------------------------------------------- ADD TO DICT

def create_index():
    global custom_games

    game_index = []
    {game_index.append(x) for x in range(len(game_title))}

    # ---------------------------------------- Add game indices
    for x in range(len(game_index)):
        custom_games = dict.fromkeys(game_index, {})


def add_to_dict():
    global custom_games

    # ---------------------------------------- Add game title
    custom_games = {x: {"game_title": game_title[x]}
                    for x in range(len(custom_games))}

    # ---------------------------------------- Add game img
    for x in range(len(custom_games)):
        upd_dict = {"game_img_full": game_img[x]}
        custom_games[x].update(upd_dict)

    # ---------------------------------------- Add game screenshots
    for x in range(len(custom_games)):
        upd_dict = {"screenshots": game_screenshots[x]}
        custom_games[x].update(upd_dict)

    # ---------------------------------------- Add game tags
    for x in range(len(custom_games)):
        upd_dict = {"game_top_tags": game_tags[x]}
        custom_games[x].update(upd_dict)

    # ---------------------------------------- Add game platform tags
    for x in range(len(custom_games)):
        upd_dict = {"platform_tags_pc": game_platform_tags[x]}
        custom_games[x].update(upd_dict)

    # ---------------------------------------- Add game links
    for x in range(len(custom_games)):
        upd_dict = {"game_link": links[x]}
        custom_games[x].update(upd_dict)

    # ---------------------------------------- Add game summary
    for x in range(len(custom_games)):
        upd_dict = {"game_summary": game_summary[x]}
        custom_games[x].update(upd_dict)

    # ---------------------------------------- Add game categories
    for x in range(len(custom_games)):
        for y in range(len(categories[x])):
            upd_dict = {categories[x][y]: True}
            custom_games[x].update(upd_dict)

    # ---------------------------------------- Add liked by
    for x in range(len(custom_games)):
        upd_dict = {"liked_by": None}
        custom_games[x].update(upd_dict)

    # ---------------------------------------- Add likes
    for x in range(len(custom_games)):
        upd_dict = {"likes": 0}
        custom_games[x].update(upd_dict)


grab_links()
scrape_data()
create_index()
add_to_dict()
