import requests
from bs4 import BeautifulSoup

"""
Some of the code is based upon the following sources:

    Splitting elements with BeautifulSoup:
    "https://stackoverflow.com/questions/12616912/split-an-element-with-beautifulsoup"

    Getting href tags with BeautifulSoup:
    "https://stackoverflow.com/questions/43814754/python-beautifulsoup-how-to-get-href-attribute-of-a-element/43814994"
"""

# -------------------------------------------------- Data lists

# -------------- Bestsellers

bs_game_titles = []
bs_game_tags = []
bs_game_links = []
bs_game_images = []
bs_game_platform_tags = []


# ------------------------------------------- Scrape data function


# ----------------------------------------------------------------- BESTSELLERS


def scrape_bestsellers():

    bestsellers_url = "https://store.steampowered.com/games/#p=0&tab=TopSellers"

    source = requests.get(bestsellers_url)
    soup = BeautifulSoup(source.text, "html.parser")

    for item in soup.select("#TopSellersRows"):
        for a in item.findAll("a", href=True):

            # -------------------------------------------------- Game Titles

            title = a.select(".tab_item_name")
            for i in title:
                title_string = i.string
                bs_game_titles.append(title_string)

            # -------------------------------------------------- Game Tags

            top_tags = a.select(".tab_item_top_tags span")

            tags = []
            tags_inner = []

            for items in top_tags:
                for tag in items:
                    tag_item = tag.string

                    if tag_item[0] == ",":
                        tags_inner.append(tag_item)
                    else:
                        tag_item = [tag_item]
                        tags.append(tag_item)

            for i in tags_inner:
                tags[0].append(i)

            for tag in tags:
                bs_game_tags.append(tag)

            # -------------------------------------------------- Game Links

            link = a.attrs["href"]
            bs_game_links.append(link)

            # -------------------------------------------------- Game img src

            game_image = a.select(".tab_item_cap_img")
            for image in game_image:
                bs_game_images.append(image["src"])

            # ---------------------------------------------- Game platform tags

            pc_platforms = a.select(".tab_item_details .platform_img")

            platforms = str(pc_platforms)

            for i in range(len(platforms)):
                platforms = platforms.replace(
                    '<span class="platform_img win"></span>', 'win'
                ).replace(
                    '<span class="platform_img mac"></span>', 'mac'
                ).replace(
                    '<span class="platform_img linux"></span>', 'linux'
                )

            bs_game_platform_tags.append(platforms)


# --------------------------------------------------------------- AWARD WINNERS

def scrape_awardwinners():
    awardwinners_url = "https://store.steampowered.com/steamawards"

    source = requests.get(awardwinners_url)
    soup = BeautifulSoup(source.text, "html.parser")

    for item in soup.select(".vote_category_bg"):
        for div in item.select(".vote_category_ctn"):
            for i in div.findAll("div"):

                for category in i.select(".category_title_ctn"):

                    award_year = category.select(".category_year")
                    award_title = category.select(".category_title")

                    print(award_year, award_title)


# ------------------ Call scrape data functions


scrape_bestsellers()

scrape_awardwinners()


# ------------------------------------------- Dictionaries

steam_bestsellers = {}

# ----------------------------------------------------------------- BESTSELLERS


def create_bestsellers_index():
    global steam_bestsellers

    game_index = []
    {game_index.append(x) for x in range(len(bs_game_titles))}

    # ---------------------------------------- Add game indices
    for x in range(len(game_index)):
        steam_bestsellers = dict.fromkeys(game_index, {})


def add_to_bestsellers_dict():
    global steam_bestsellers

    # ---------------------------------------- Add game titles
    steam_bestsellers = {x: {"title": bs_game_titles[x]}
                         for x in range(len(steam_bestsellers))}

    # ---------------------------------------- Add game tags
    for x in range(len(bs_game_tags)):
        upd_dict = {"tags": bs_game_tags[x]}
        steam_bestsellers[x].update(upd_dict)

    # ---------------------------------------- Add game images
    for x in range(len(steam_bestsellers)):
        upd_dict = {"image": bs_game_images[x]}
        steam_bestsellers[x].update(upd_dict)

    # ---------------------------------------- Add game platform tags
    for x in range(len(steam_bestsellers)):
        upd_dict = {"pc_platform_tags": bs_game_platform_tags[x]}
        steam_bestsellers[x].update(upd_dict)

    # ---------------------------------------- Add game links
    for x in range(len(steam_bestsellers)):
        upd_dict = {"game_link": bs_game_links[x]}
        steam_bestsellers[x].update(upd_dict)


# ------------------ Call add to dictionary functions


create_bestsellers_index()
add_to_bestsellers_dict()
