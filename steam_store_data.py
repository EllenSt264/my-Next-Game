import requests
from bs4 import BeautifulSoup

bestsellers_url = "https://store.steampowered.com/games/#p=0&tab=TopSellers"

source = requests.get(bestsellers_url)
soup = BeautifulSoup(source.text, "html.parser")


def scrape_data():
    for item in soup.select("#TopSellersRows"):
        for a in item.findAll("a", href=True):
            title = a.select(".tab_item_name")
            print(title)
