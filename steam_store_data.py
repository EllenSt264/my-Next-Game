import requests
from bs4 import BeautifulSoup

bestsellers_url = "https://store.steampowered.com/games/#p=0&tab=TopSellers"

source = requests.get(bestsellers_url)
soup = BeautifulSoup(source.text, "html.parser")


"""
Sources: "https://stackoverflow.com/questions/12616912/split-an-element-with-beautifulsoup"
"""

# -------------------------------------------------- Data lists
game_titles = []
game_tags = []


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


scrape_data()
