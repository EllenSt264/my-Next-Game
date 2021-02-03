import requests
from bs4 import BeautifulSoup

bestsellers_url = "https://store.steampowered.com/games/#p=0&tab=TopSellers"

source = requests.get(bestsellers_url)
soup = BeautifulSoup(source.text, "html.parser")


"""
Some of the code is based upon the following sources:

    Splitting elements with BeautifulSoup:
    "https://stackoverflow.com/questions/12616912/split-an-element-with-beautifulsoup"

    Getting href tags with BeautifulSoup:
    "https://stackoverflow.com/questions/43814754/python-beautifulsoup-how-to-get-href-attribute-of-a-element/43814994"
"""

# -------------------------------------------------- Data lists
game_titles = []
game_tags = []
game_links = []
game_images = []
game_platform_tags = []


def scrape_data():

    for item in soup.select("#TopSellersRows"):
        for a in item.findAll("a", href=True):

            # -------------------------------------------------- Game Titles

            title = a.select(".tab_item_name")
            for i in title:
                title_string = i.string
                game_titles.append(title_string)

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
                game_tags.append(tag)

            # -------------------------------------------------- Game Links

            link = a.attrs["href"]
            game_links.append(link)

            # -------------------------------------------------- Game img src

            game_image = a.select(".tab_item_cap_img")
            for image in game_image:
                game_images.append(image["src"])

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

            game_platform_tags.append(platforms)


scrape_data()


# -------------------------------------------------- Dictionary

steam_bestsellers = {}


def create_index():
    global steam_bestsellers

    game_index = []
    for x in range(len(game_titles)):
        game_index.append(x)

    # ---------------------------------------- Add game indices
    for x in range(len(game_index)):
        steam_bestsellers = dict.fromkeys(game_index, {})


def add_to_dict():
    global steam_bestsellers

    # ---------------------------------------- Add game titles
    for x in range(len(steam_bestsellers)):
        steam_bestsellers[x] = {"title": game_titles[x]}

    # ---------------------------------------- Add game tags
    for x in range(len(steam_bestsellers)):
        upd_dict = {"tags": game_tags[x]}
        steam_bestsellers[x].update(upd_dict)

    # ---------------------------------------- Add game images
    for x in range(len(steam_bestsellers)):
        upd_dict = {"image": game_images[x]}
        steam_bestsellers[x].update(upd_dict)

    # ---------------------------------------- Add game platform tags
    for x in range(len(steam_bestsellers)):
        upd_dict = {"pc_platform_tags": game_platform_tags[x]}
        steam_bestsellers[x].update(upd_dict)

    # ---------------------------------------- Add game links
    for x in range(len(steam_bestsellers)):
        upd_dict = {"game_link": game_links[x]}
        steam_bestsellers[x].update(upd_dict)


create_index()
add_to_dict()
