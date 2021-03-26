"""
** Attribution:

    Splitting elements with BeautifulSoup:
    "https://stackoverflow.com/questions/12616912/split-an-element-with-beautifulsoup"

    Getting href tags with BeautifulSoup:
    "https://stackoverflow.com/questions/43814754/python-beautifulsoup-how-to-get-href-attribute-of-a-element/43814994"

    Looping through a list or URLs with BeautifulSoup:
    "https://stackoverflow.com/questions/44823278/how-to-loop-through-a-list-of-urls-for-web-scraping-with-beautifulsoup"

    Fix 'RuntimeError: dictionary changed size during iteration':
    "https://stackoverflow.com/questions/11941817/how-to-avoid-runtimeerror-dictionary-changed-size-during-iteration-error"

    Remove whitespace:
    "https://stackoverflow.com/questions/53424179/beautifulsoup-stripping-whitespace"

    To get past the website's age check:
    "https://stackoverflow.com/questions/33603416/python-beautiful-soup-getting-past-steams-age-check"

    Remove string control characters:
    "https://moonbooks.org/Articles/How-to-remove-string-control-characters-n-t-r-in-python/"

    Help with the join method to return the first few sentences of a paragraph:
    "https://runestone.academy/runestone/books/published/fopp/Sequences/SplitandJoin.html"

"""

import re
import requests
from bs4 import BeautifulSoup

# -------------------------------------------------- Data lists

# -------------- Bestsellers

bs_game_titles = []
bs_bundle_game_tags = []
bs_game_tags = []
bs_game_links = []
bs_game_images = []
bs_game_images_full = []
bs_game_platform_tags = []

# -------------- Award Winners

award_year = []
award_title = []
award_winner = []
award_winner_img = []
award_game_links = []
award_game_tags = []
award_game_platform_tags = []

# -------------- Action Games

action_titles = []
action_bundle_game_tags = []
action_tags = []
action_links = []
action_images = []
action_full_images = []
action_platform_tags = []

# -------------- Adventure Games

adventure_titles = []
adventure_bundle_game_tags = []
adventure_tags = []
adventure_links = []
adventure_images = []
adventure_full_images = []
adventure_platform_tags = []

# -------------- RPG Games

RPG_titles = []
RPG_bundle_game_tags = []
RPG_tags = []
RPG_links = []
RPG_images = []
RPG_full_images = []
RPG_platform_tags = []

# -------------- Strategy Games

strategy_titles = []
strategy_bundle_game_tags = []
strategy_tags = []
strategy_links = []
strategy_images = []
strategy_full_images = []
strategy_platform_tags = []

# -------------- Multiplayer Games

multiplayer_titles = []
multiplayer_bundle_game_tags = []
multiplayer_tags = []
multiplayer_links = []
multiplayer_images = []
multiplayer_full_images = []
multiplayer_platform_tags = []

# -------------- Favourites

# Links have been added manually
favourite_links = [
    "https://store.steampowered.com/app/1174180/Red_Dead_Redemption_2/",
    "https://store.steampowered.com/app/1404210/Red_Dead_Online/",
    "https://store.steampowered.com/app/379430/Kingdom_Come_Deliverance/",
    "https://store.steampowered.com/app/261550/Mount__Blade_II_Bannerlord/",
    "https://store.steampowered.com/app/1158310/Crusader_Kings_III/",
    "https://store.steampowered.com/app/629760/MORDHAU/",
    "https://store.steampowered.com/app/427290/Vampyr/",
    "https://store.steampowered.com/app/752590/A_Plague_Tale_Innocence/",
    "https://store.steampowered.com/app/409710/BioShock_Remastered/",
    "https://store.steampowered.com/app/1328670/Mass_Effect_Legendary_Edition/",
    "https://store.steampowered.com/app/703080/Planet_Zoo/",
    "https://store.steampowered.com/app/493340/Planet_Coaster/",
    "https://store.steampowered.com/app/1237950/STAR_WARS_Battlefront_II/",
    "https://store.steampowered.com/app/281990/Stellaris/",
    "https://store.steampowered.com/app/238320/Outlast/",
    "https://store.steampowered.com/app/480490/Prey/",
    "https://store.steampowered.com/app/271590/Grand_Theft_Auto_V/",
    "https://store.steampowered.com/app/362890/Black_Mesa/",
    "https://store.steampowered.com/app/1190460/DEATH_STRANDING/",
    "https://store.steampowered.com/app/489830/The_Elder_Scrolls_V_Skyrim_Special_Edition/",
    "https://store.steampowered.com/app/900883/The_Elder_Scrolls_IV_Oblivion_Game_of_the_Year_Edition_Deluxe/",
    "https://store.steampowered.com/app/306130/The_Elder_Scrolls_Online/",
    "https://store.steampowered.com/app/379720/DOOM/"
]

favourites_game_title = []
favourites_game_img = []
favourites_game_screenshots = []
favourites_game_tags = []
favourites_platform_pc = []
favourite_game_summary = []


# ------------------------------------------- Scrape data functions


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
            bs_game_platform_tags.append(platform_lis)


# Scrape data from the each game page
def scrape_bestseller_game_page():
    url_list = bs_game_links

    bundle_url_list = []

    for url in url_list:
        # Define cookies in order to bypass age check
        cookies = {"birthtime": "786240001", "lastagecheckage": "1-0-1995"}
        source = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(source.text, "html.parser")

        # ------------------------------ Game full image

        for item in soup.select(".page_content_ctn"):
            if item.find("img", {"class": "package_header"}):
                img = item.select(".package_header")
                for i in img:
                    bs_game_images_full.append(i["src"])

            else:
                img = item.select(".game_header_image_full")
                for i in img:
                    bs_game_images_full.append(i["src"])

        # ------------------------------ Game genre tags

        bundle = soup.select("#package_header_container")

        if bundle:
            a = soup.find("a", {"class": "tab_item_overlay"})
            if a is None:
                continue
            else:
                link = a.attrs["href"]
                bundle_url_list.append(link)
                bs_game_tags.append(["bundle"])
        else:
            # ------------------------------ Game genre tags

            tags_inner = []

            for item in soup.select(".glance_tags.popular_tags"):
                for a in item.select("a", href=True):
                    tag = a.text.strip()
                    tags_inner.append(tag)

            bs_game_tags.append(tags_inner)

    # Grab data from the links acquired on the bundle page

    bundle_tags = []

    for url in bundle_url_list:
        cookies = {"birthtime": "786240001", "lastagecheckage": "1-0-1995"}
        source = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(source.text, "html.parser")

        # ------------------------------ Game genre tags
        tags_inner = []

        for item in soup.select(".glance_tags.popular_tags"):
            for a in item.select("a", href=True):
                tag = a.text.strip()
                tags_inner.append(tag)

        bundle_tags.append(tags_inner)

    global bs_bundle_game_tags
    bs_bundle_game_tags = bundle_tags

    # Replace game tags list bundle' item with list item from bundle tags
    bundleIndex = 0
    for lis in bs_game_tags:
        while "bundle" in lis:
            lis[lis.index("bundle")] = bs_bundle_game_tags[bundleIndex]
            bundleIndex += 1


# --------------------------------------------------------------- AWARD WINNERS

def scrape_awardwinners():
    awardwinners_url = "https://store.steampowered.com/steamawards"

    source = requests.get(awardwinners_url)
    soup = BeautifulSoup(source.text, "html.parser")

    for item in soup.select(".vote_category_bg"):
        for div in item.select(".vote_category_ctn"):
            for i in div.findAll("div"):

                # ----------------------------------------- Award Category

                for category in i.select(".category_title_ctn"):

                    aw_year = category.select(".category_year")
                    aw_title = category.select(".category_title")

                    # Award Year
                    for year in aw_year:
                        award_year.append(year.text)

                    # Award title
                    for title in aw_title:
                        award_title.append(title.text)

                # ----------------------------------------- Winner Category

                for category in i.select(".category_winner_ctn"):

                    # ---------------------------------------------- Game Links

                    for a in category.select("a", href=True):
                        link = a.attrs["href"]
                        award_game_links.append(link)

                    # ------------------------------ Winner img

                    winner_img = category.select(".category_winner_capsule")
                    for img in winner_img:
                        award_winner_img.append(img["src"])

                    # ------------------------------ Winner name

                    for winner in category.select(".winner_description_ctn"):

                        winner = winner.select(".winner_name")
                        for game in winner:
                            award_winner.append(game.string)


# Scrape data from the each game page
def scrape_awardwinner_game_page():
    url_list = award_game_links

    for url in url_list:

        cookies = {"birthtime": "786240001", "lastagecheckage": "1-0-1995"}
        source = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(source.text, "html.parser")

        # ------------------------------ Game genre tags

        tags_inner = []

        for item in soup.select(".glance_tags.popular_tags"):
            for a in item.select("a", href=True, limit=5):
                tag = a.text.strip()
                tags_inner.append(tag)

        award_game_tags.append(tags_inner)

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
            award_game_platform_tags.append(platform_lis)


# -------------------------------------------------------------------- ACTION

def scrape_action_games():
    url = "https://store.steampowered.com/tags/en/Action/#p=0&tab=TopRated"

    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")

    for item in soup.select("#TopRatedRows"):
        for a in item.findAll("a", href=True):

            # -------------------------------------------------- Game Titles

            title = a.select(".tab_item_name")
            for i in title:
                title_string = i.string
                action_titles.append(title_string)

            # -------------------------------------------------- Game Links

            link = a.attrs["href"]
            action_links.append(link)

            # -------------------------------------------------- Game img src

            game_image = a.select(".tab_item_cap_img")
            for image in game_image:
                action_images.append(image["src"])

            # ---------------------------------------------- Game platform tags

            pc_platforms = a.select(".tab_item_details .platform_img")

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
            action_platform_tags.append(platform_lis)


# Scrape data from the each game page
def scrape_action_game_page():
    url_list = action_links

    bundle_url_list = []

    for url in url_list:
        # Define cookies in order to bypass age check
        cookies = {"birthtime": "786240001", "lastagecheckage": "1-0-1995"}
        source = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(source.text, "html.parser")

        # ------------------------------ Game full image

        for item in soup.select(".page_content_ctn"):
            if item.find("img", {"class": "package_header"}):
                img = item.select(".package_header")
                for i in img:
                    action_full_images.append(i["src"])

            else:
                img = item.select(".game_header_image_full")
                for i in img:
                    action_full_images.append(i["src"])

        # ------------------------------ Game genre tags

        bundle = soup.select("#package_header_container")

        if bundle:
            a = soup.find("a", {"class": "tab_item_overlay"})
            if a is None:
                continue
            else:
                link = a.attrs["href"]
                bundle_url_list.append(link)
                action_tags.append(["bundle"])
        else:
            # ------------------------------ Game genre tags

            tags_inner = []

            for item in soup.select(".glance_tags.popular_tags"):
                for a in item.select("a", href=True):
                    tag = a.text.strip()
                    tags_inner.append(tag)

            action_tags.append(tags_inner)

    # Grab data from the links acquired on the bundle page

    bundle_tags = []

    for url in bundle_url_list:
        cookies = {"birthtime": "786240001", "lastagecheckage": "1-0-1995"}
        source = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(source.text, "html.parser")

        # ------------------------------ Game genre tags
        tags_inner = []

        for item in soup.select(".glance_tags.popular_tags"):
            for a in item.select("a", href=True):
                tag = a.text.strip()
                tags_inner.append(tag)

        bundle_tags.append(tags_inner)

    global action_bundle_game_tags
    action_bundle_game_tags = bundle_tags

    # Replace game tags list bundle' item with list item from bundle tags
    bundleIndex = 0
    for lis in action_tags:
        while "bundle" in lis:
            lis[lis.index("bundle")] = action_bundle_game_tags[bundleIndex]
            bundleIndex += 1


# -------------------------------------------------------------------- AVENTURE

def scrape_adventure_games():
    url = "https://store.steampowered.com/tags/en/Adventure/#p=0&tab=TopRated"

    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")

    for item in soup.select("#TopRatedRows"):
        for a in item.findAll("a", href=True):

            # -------------------------------------------------- Game Titles

            title = a.select(".tab_item_name")
            for i in title:
                title_string = i.string
                adventure_titles.append(title_string)

            # -------------------------------------------------- Game Links

            link = a.attrs["href"]
            adventure_links.append(link)

            # -------------------------------------------------- Game img src

            game_image = a.select(".tab_item_cap_img")
            for image in game_image:
                adventure_images.append(image["src"])

            # ---------------------------------------------- Game platform tags

            pc_platforms = a.select(".tab_item_details .platform_img")

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
            adventure_platform_tags.append(platform_lis)


# Scrape data from the each game page
def scrape_adventure_game_page():
    url_list = adventure_links

    bundle_url_list = []

    for url in url_list:
        # Define cookies in order to bypass age check
        cookies = {"birthtime": "786240001", "lastagecheckage": "1-0-1995"}
        source = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(source.text, "html.parser")

        # ------------------------------ Game full image

        for item in soup.select(".page_content_ctn"):
            if item.find("img", {"class": "package_header"}):
                img = item.select(".package_header")
                for i in img:
                    adventure_full_images.append(i["src"])

            else:
                img = item.select(".game_header_image_full")
                for i in img:
                    adventure_full_images.append(i["src"])

        # ------------------------------ Game genre tags

        bundle = soup.select("#package_header_container")

        if bundle:
            a = soup.find("a", {"class": "tab_item_overlay"})
            if a is None:
                continue
            else:
                link = a.attrs["href"]
                bundle_url_list.append(link)
                adventure_tags.append(["bundle"])
        else:
            # ------------------------------ Game genre tags

            tags_inner = []

            for item in soup.select(".glance_tags.popular_tags"):
                for a in item.select("a", href=True):
                    tag = a.text.strip()
                    tags_inner.append(tag)

            adventure_tags.append(tags_inner)

    # Grab data from the links acquired on the bundle page

    bundle_tags = []

    for url in bundle_url_list:
        cookies = {"birthtime": "786240001", "lastagecheckage": "1-0-1995"}
        source = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(source.text, "html.parser")

        # ------------------------------ Game genre tags
        tags_inner = []

        for item in soup.select(".glance_tags.popular_tags"):
            for a in item.select("a", href=True):
                tag = a.text.strip()
                tags_inner.append(tag)

        bundle_tags.append(tags_inner)

    global adventure_bundle_game_tags
    adventure_bundle_game_tags = bundle_tags

    # Replace game tags list bundle' item with list item from bundle tags
    bundleIndex = 0
    for lis in adventure_tags:
        while "bundle" in lis:
            lis[lis.index("bundle")] = adventure_bundle_game_tags[bundleIndex]
            bundleIndex += 1


# -------------------------------------------------------------------- RPG

def scrape_RPG_games():
    url = "https://store.steampowered.com/tags/en/RPG/#p=0&tab=TopRated"

    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")

    for item in soup.select("#TopRatedRows"):
        for a in item.findAll("a", href=True):

            # -------------------------------------------------- Game Titles

            title = a.select(".tab_item_name")
            for i in title:
                title_string = i.string
                RPG_titles.append(title_string)

            # -------------------------------------------------- Game Links

            link = a.attrs["href"]
            RPG_links.append(link)

            # -------------------------------------------------- Game img src

            game_image = a.select(".tab_item_cap_img")
            for image in game_image:
                RPG_images.append(image["src"])

            # ---------------------------------------------- Game platform tags

            pc_platforms = a.select(".tab_item_details .platform_img")

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
            RPG_platform_tags.append(platform_lis)


# Scrape data from the each game page
def scrape_RPG_game_page():
    url_list = RPG_links

    bundle_url_list = []

    for url in url_list:
        # Define cookies in order to bypass age check
        cookies = {"birthtime": "786240001", "lastagecheckage": "1-0-1995"}
        source = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(source.text, "html.parser")

        # ------------------------------ Game full image

        for item in soup.select(".page_content_ctn"):
            if item.find("img", {"class": "package_header"}):
                img = item.select(".package_header")
                for i in img:
                    RPG_full_images.append(i["src"])

            else:
                img = item.select(".game_header_image_full")
                for i in img:
                    RPG_full_images.append(i["src"])

        # ------------------------------ Game genre tags

        bundle = soup.select("#package_header_container")

        if bundle:
            a = soup.find("a", {"class": "tab_item_overlay"})
            if a is None:
                continue
            else:
                link = a.attrs["href"]
                bundle_url_list.append(link)
                RPG_tags.append(["bundle"])
        else:
            # ------------------------------ Game genre tags

            tags_inner = []

            for item in soup.select(".glance_tags.popular_tags"):
                for a in item.select("a", href=True):
                    tag = a.text.strip()
                    tags_inner.append(tag)

            RPG_tags.append(tags_inner)

    # Grab data from the links acquired on the bundle page

    bundle_tags = []

    for url in bundle_url_list:
        cookies = {"birthtime": "786240001", "lastagecheckage": "1-0-1995"}
        source = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(source.text, "html.parser")

        # ------------------------------ Game genre tags
        tags_inner = []

        for item in soup.select(".glance_tags.popular_tags"):
            for a in item.select("a", href=True):
                tag = a.text.strip()
                tags_inner.append(tag)

        bundle_tags.append(tags_inner)

    global RPG_bundle_game_tags
    RPG_bundle_game_tags = bundle_tags

    # Replace game tags list bundle' item with list item from bundle tags
    bundleIndex = 0
    for lis in RPG_tags:
        while "bundle" in lis:
            lis[lis.index("bundle")] = RPG_bundle_game_tags[bundleIndex]
            bundleIndex += 1


# -------------------------------------------------------------------- STRATEGY

def scrape_strategy_games():
    url = "https://store.steampowered.com/tags/en/Strategy/#p=0&tab=TopRated"

    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")

    for item in soup.select("#TopRatedRows"):
        for a in item.findAll("a", href=True):

            # -------------------------------------------------- Game Titles

            title = a.select(".tab_item_name")
            for i in title:
                title_string = i.string
                strategy_titles.append(title_string)

            # -------------------------------------------------- Game Links

            link = a.attrs["href"]
            strategy_links.append(link)

            # -------------------------------------------------- Game img src

            game_image = a.select(".tab_item_cap_img")
            for image in game_image:
                strategy_images.append(image["src"])

            # ---------------------------------------------- Game platform tags

            pc_platforms = a.select(".tab_item_details .platform_img")

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
            strategy_platform_tags.append(platform_lis)


# Scrape data from the each game page
def scrape_strategy_game_page():
    url_list = strategy_links

    bundle_url_list = []

    for url in url_list:
        # Define cookies in order to bypass age check
        cookies = {"birthtime": "786240001", "lastagecheckage": "1-0-1995"}
        source = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(source.text, "html.parser")

        # ------------------------------ Game full image

        for item in soup.select(".page_content_ctn"):
            if item.find("img", {"class": "package_header"}):
                img = item.select(".package_header")
                for i in img:
                    strategy_full_images.append(i["src"])

            else:
                img = item.select(".game_header_image_full")
                for i in img:
                    strategy_full_images.append(i["src"])

        # ------------------------------ Game genre tags

        bundle = soup.select("#package_header_container")

        if bundle:
            a = soup.find("a", {"class": "tab_item_overlay"})
            if a is None:
                continue
            else:
                link = a.attrs["href"]
                bundle_url_list.append(link)
                strategy_tags.append(["bundle"])
        else:
            # ------------------------------ Game genre tags

            tags_inner = []

            for item in soup.select(".glance_tags.popular_tags"):
                for a in item.select("a", href=True):
                    tag = a.text.strip()
                    tags_inner.append(tag)

            strategy_tags.append(tags_inner)

    # Grab data from the links acquired on the bundle page

    bundle_tags = []

    for url in bundle_url_list:
        cookies = {"birthtime": "786240001", "lastagecheckage": "1-0-1995"}
        source = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(source.text, "html.parser")

        # ------------------------------ Game genre tags
        tags_inner = []

        for item in soup.select(".glance_tags.popular_tags"):
            for a in item.select("a", href=True):
                tag = a.text.strip()
                tags_inner.append(tag)

        bundle_tags.append(tags_inner)

    global strategy_bundle_game_tags
    strategy_bundle_game_tags = bundle_tags

    # Replace game tags list bundle' item with list item from bundle tags
    bundleIndex = 0
    for lis in strategy_tags:
        while "bundle" in lis:
            lis[lis.index("bundle")] = strategy_bundle_game_tags[bundleIndex]
            bundleIndex += 1


# ----------------------------------------------------------------- MULTIPLAYER

def scrape_multiplayer_games():
    url = "https://store.steampowered.com/tags/en/Massively%20Multiplayer/#p=0&tab=TopRated"

    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")

    for item in soup.select("#TopRatedRows"):
        for a in item.findAll("a", href=True):

            # -------------------------------------------------- Game Titles

            title = a.select(".tab_item_name")
            for i in title:
                title_string = i.string
                multiplayer_titles.append(title_string)

            # -------------------------------------------------- Game Links

            link = a.attrs["href"]
            multiplayer_links.append(link)

            # -------------------------------------------------- Game img src

            game_image = a.select(".tab_item_cap_img")
            for image in game_image:
                multiplayer_images.append(image["src"])

            # ---------------------------------------------- Game platform tags

            pc_platforms = a.select(".tab_item_details .platform_img")

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
            multiplayer_platform_tags.append(platform_lis)


# Scrape data from the each game page
def scrape_multiplayer_game_page():
    url_list = multiplayer_links

    bundle_url_list = []

    for url in url_list:
        # Define cookies in order to bypass age check
        cookies = {"birthtime": "786240001", "lastagecheckage": "1-0-1995"}
        source = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(source.text, "html.parser")

        # ------------------------------ Game full image

        for item in soup.select(".page_content_ctn"):
            if item.find("img", {"class": "package_header"}):
                img = item.select(".package_header")
                for i in img:
                    multiplayer_full_images.append(i["src"])

            else:
                img = item.select(".game_header_image_full")
                for i in img:
                    multiplayer_full_images.append(i["src"])

        # ------------------------------ Game genre tags

        bundle = soup.select("#package_header_container")

        if bundle:
            a = soup.find("a", {"class": "tab_item_overlay"})
            if a is None:
                continue
            else:
                link = a.attrs["href"]
                bundle_url_list.append(link)
                multiplayer_tags.append(["bundle"])
        else:
            # ------------------------------ Game genre tags

            tags_inner = []

            for item in soup.select(".glance_tags.popular_tags"):
                for a in item.select("a", href=True):
                    tag = a.text.strip()
                    tags_inner.append(tag)

            multiplayer_tags.append(tags_inner)

    # Grab data from the links acquired on the bundle page

    bundle_tags = []

    for url in bundle_url_list:
        cookies = {"birthtime": "786240001", "lastagecheckage": "1-0-1995"}
        source = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(source.text, "html.parser")

        # ------------------------------ Game genre tags
        tags_inner = []

        for item in soup.select(".glance_tags.popular_tags"):
            for a in item.select("a", href=True):
                tag = a.text.strip()
                tags_inner.append(tag)

        bundle_tags.append(tags_inner)

    global multiplayer_bundle_game_tags
    multiplayer_bundle_game_tags = bundle_tags

    # Replace game tags list bundle' item with list item from bundle tags
    bundleIndex = 0
    for lis in multiplayer_tags:
        while "bundle" in lis:
            lis[lis.index("bundle")] = multiplayer_bundle_game_tags[bundleIndex]
            bundleIndex += 1


# ----------------------------------------------------------------- FAVOURITES

def scrape_favourites_data():
    url_list = favourite_links

    for url in url_list:

        cookies = {"birthtime": "786240001", "lastagecheckage": "1-0-1995"}
        source = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(source.text, "html.parser")

        # ------------------------------ Game title
        for item in soup.select(".page_title_area.game_title_area"):
            for title in item.select(".apphub_AppName"):
                favourites_game_title.append(title.text)

        # ------------------------------ Game image

        for item in soup.select(".page_content_ctn"):
            if item.find("img", {"class": "package_header"}):
                img = item.select(".package_header")
                for i in img:
                    favourites_game_img.append(i["src"])

            else:
                img = item.select(".game_header_image_full")
                for i in img:
                    favourites_game_img.append(i["src"])

        # ------------------------------ Game image - screenshots

        screenshots = []

        for item in soup.select(".highlight_player_item.highlight_screenshot"):
            for i in item.select(".screenshot_holder"):
                images = i.select(".highlight_screenshot_link", href=True)
                for img in images:
                    screenshots.append(img.attrs["href"])

        favourites_game_screenshots.append(screenshots)

        # ------------------------------ Game genre tags

        tags_inner = []

        for item in soup.select(".glance_tags.popular_tags"):
            for a in item.select("a", href=True, limit=5):
                tag = a.text.strip()
                tags_inner.append(tag)

        favourites_game_tags.append(tags_inner)

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
            favourites_platform_pc.append(platform_lis)

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

            favourite_game_summary.append(summary_str)


# ------------------ Call scrape data functions

scrape_bestsellers()
scrape_bestseller_game_page()

scrape_awardwinners()
scrape_awardwinner_game_page()

scrape_action_games()
scrape_action_game_page()

scrape_adventure_games()
scrape_adventure_game_page()

scrape_RPG_games()
scrape_RPG_game_page()

scrape_strategy_games()
scrape_strategy_game_page()

scrape_multiplayer_games()
scrape_multiplayer_game_page()

scrape_favourites_data()


# ------------------------------------------- Dictionaries

steam_bestsellers = {}

steam_award_winners = {}

steam_action_games = {}

steam_adventure_games = {}

steam_RPG_games = {}

steam_strategy_games = {}

steam_multiplayer_games = {}

favourites = {}


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

    # ---------------------------------------- Add full game image
    for x in range(len(bs_game_images_full)):
        upd_dict = {"full_image": bs_game_images_full[x]}
        steam_bestsellers[x].update(upd_dict)

    # ---------------------------------------- Add game platform tags
    for x in range(len(steam_bestsellers)):
        upd_dict = {"pc_platform_tags": bs_game_platform_tags[x]}
        steam_bestsellers[x].update(upd_dict)

    # ---------------------------------------- Add game links
    for x in range(len(steam_bestsellers)):
        upd_dict = {"game_link": bs_game_links[x]}
        steam_bestsellers[x].update(upd_dict)


# --------------------------------------------------------------- AWARD WINNERS

def create_awardwinners_index():
    global steam_award_winners

    game_index = []
    {game_index.append(x) for x in range(len(award_title))}

    # ---------------------------------------- Add game indices
    for x in range(len(game_index)):
        steam_award_winners = dict.fromkeys(game_index, {})


def add_to_awardwinners_dict():
    global steam_award_winners

    # ---------------------------------------- Add award year
    steam_award_winners = {x: {"year": award_year[x]}
                           for x in range(len(steam_award_winners))}

    # ---------------------------------------- Add award title
    for x in range(len(steam_award_winners)):
        upd_dict = {"award": award_title[x]}
        steam_award_winners[x].update(upd_dict)

    # ---------------------------------------- Add award winner
    for x in range(len(steam_award_winners)):
        upd_dict = {"winner": award_winner[x]}
        steam_award_winners[x].update(upd_dict)

    # ---------------------------------------- Add game img
    for x in range(len(steam_award_winners)):
        upd_dict = {"img": award_winner_img[x]}
        steam_award_winners[x].update(upd_dict)

    # ---------------------------------------- Add game tags
    for x in range(len(steam_award_winners)):
        upd_dict = {"tags": award_game_tags[x]}
        steam_award_winners[x].update(upd_dict)

    # ---------------------------------------- Add game platform tags
    for x in range(len(steam_award_winners)):
        upd_dict = {"pc_platform_tags": award_game_platform_tags[x]}
        steam_award_winners[x].update(upd_dict)

    # ---------------------------------------- Add game links
    for x in range(len(steam_award_winners)):
        upd_dict = {"game_link": award_game_links[x]}
        steam_award_winners[x].update(upd_dict)


# ---------------------------------------------------------------- ACTION GAMES

def create_action_games_index():
    global steam_action_games

    game_index = []
    {game_index.append(x) for x in range(len(action_titles))}

    # ---------------------------------------- Add game indices
    for x in range(len(game_index)):
        steam_action_games = dict.fromkeys(game_index, {})


def add_to_action_games_dict():
    global steam_action_games

    # ---------------------------------------- Add game titles
    steam_action_games = {x: {"title": action_titles[x]}
                          for x in range(len(steam_action_games))}

    # ---------------------------------------- Add game tags
    for x in range(len(action_tags)):
        upd_dict = {"tags": action_tags[x]}
        steam_action_games[x].update(upd_dict)

    # ---------------------------------------- Add game image
    for x in range(len(steam_action_games)):
        upd_dict = {"image": action_images[x]}
        steam_action_games[x].update(upd_dict)

    # ---------------------------------------- Add full game image
    for x in range(len(steam_action_games)):
        upd_dict = {"full_image": action_full_images[x]}
        steam_action_games[x].update(upd_dict)

    # ---------------------------------------- Add game platform tags
    for x in range(len(steam_action_games)):
        upd_dict = {"pc_platform_tags": action_platform_tags[x]}
        steam_action_games[x].update(upd_dict)

    # ---------------------------------------- Add game links
    for x in range(len(steam_action_games)):
        upd_dict = {"game_link": action_links[x]}
        steam_action_games[x].update(upd_dict)


# ------------------------------------------------------------- ADVENTURE GAMES

def create_adventure_games_index():
    global steam_adventure_games

    game_index = []
    {game_index.append(x) for x in range(len(adventure_titles))}

    # ---------------------------------------- Add game indices
    for x in range(len(game_index)):
        steam_adventure_games = dict.fromkeys(game_index, {})


def add_to_adventure_games_dict():
    global steam_adventure_games

    # ---------------------------------------- Add game titles
    steam_adventure_games = {x: {"title": adventure_titles[x]}
                             for x in range(len(steam_adventure_games))}

    # ---------------------------------------- Add game tags
    for x in range(len(adventure_tags)):
        upd_dict = {"tags": adventure_tags[x]}
        steam_adventure_games[x].update(upd_dict)

    # ---------------------------------------- Add game image
    for x in range(len(steam_adventure_games)):
        upd_dict = {"image": adventure_images[x]}
        steam_adventure_games[x].update(upd_dict)

    # ---------------------------------------- Add full game image
    for x in range(len(steam_adventure_games)):
        upd_dict = {"full_image": adventure_full_images[x]}
        steam_adventure_games[x].update(upd_dict)

    # ---------------------------------------- Add game platform tags
    for x in range(len(steam_adventure_games)):
        upd_dict = {"pc_platform_tags": adventure_platform_tags[x]}
        steam_adventure_games[x].update(upd_dict)

    # ---------------------------------------- Add game links
    for x in range(len(steam_adventure_games)):
        upd_dict = {"game_link": adventure_links[x]}
        steam_adventure_games[x].update(upd_dict)


# ------------------------------------------------------------------- RPG GAMES

def create_RPG_games_index():
    global steam_RPG_games

    game_index = []
    {game_index.append(x) for x in range(len(RPG_titles))}

    # ---------------------------------------- Add game indices
    for x in range(len(game_index)):
        steam_RPG_games = dict.fromkeys(game_index, {})


def add_to_RPG_games_dict():
    global steam_RPG_games

    # ---------------------------------------- Add game titles
    steam_RPG_games = {x: {"title": RPG_titles[x]}
                       for x in range(len(steam_RPG_games))}

    # ---------------------------------------- Add game tags
    for x in range(len(RPG_tags)):
        upd_dict = {"tags": RPG_tags[x]}
        steam_RPG_games[x].update(upd_dict)

    # ---------------------------------------- Add game image
    for x in range(len(steam_RPG_games)):
        upd_dict = {"image": RPG_images[x]}
        steam_RPG_games[x].update(upd_dict)

    # ---------------------------------------- Add full game image
    for x in range(len(steam_RPG_games)):
        upd_dict = {"full_image": RPG_full_images[x]}
        steam_RPG_games[x].update(upd_dict)

    # ---------------------------------------- Add game platform tags
    for x in range(len(steam_RPG_games)):
        upd_dict = {"pc_platform_tags": RPG_platform_tags[x]}
        steam_RPG_games[x].update(upd_dict)

    # ---------------------------------------- Add game links
    for x in range(len(steam_RPG_games)):
        upd_dict = {"game_link": RPG_links[x]}
        steam_RPG_games[x].update(upd_dict)


# ------------------------------------------------------------- STRATEGY GAMES

def create_strategy_games_index():
    global steam_strategy_games

    game_index = []
    {game_index.append(x) for x in range(len(strategy_titles))}

    # ---------------------------------------- Add game indices
    for x in range(len(game_index)):
        steam_strategy_games = dict.fromkeys(game_index, {})


def add_to_strategy_games_dict():
    global steam_strategy_games

    # ---------------------------------------- Add game titles
    steam_strategy_games = {x: {"title": strategy_titles[x]}
                            for x in range(len(steam_strategy_games))}

    # ---------------------------------------- Add game tags
    for x in range(len(strategy_tags)):
        upd_dict = {"tags": strategy_tags[x]}
        steam_strategy_games[x].update(upd_dict)

    # ---------------------------------------- Add game image
    for x in range(len(steam_strategy_games)):
        upd_dict = {"image": strategy_images[x]}
        steam_strategy_games[x].update(upd_dict)

    # ---------------------------------------- Add full game image
    for x in range(len(steam_strategy_games)):
        upd_dict = {"full_image": strategy_full_images[x]}
        steam_strategy_games[x].update(upd_dict)

    # ---------------------------------------- Add game platform tags
    for x in range(len(steam_strategy_games)):
        upd_dict = {"pc_platform_tags": strategy_platform_tags[x]}
        steam_strategy_games[x].update(upd_dict)

    # ---------------------------------------- Add game links
    for x in range(len(steam_strategy_games)):
        upd_dict = {"game_link": strategy_links[x]}
        steam_strategy_games[x].update(upd_dict)


# ----------------------------------------------------------- MULTIPLAYER GAMES

def create_multiplayer_games_index():
    global steam_multiplayer_games

    game_index = []
    {game_index.append(x) for x in range(len(multiplayer_titles))}

    # ---------------------------------------- Add game indices
    for x in range(len(game_index)):
        steam_multiplayer_games = dict.fromkeys(game_index, {})


def add_to_multiplayer_games_dict():
    global steam_multiplayer_games

    # ---------------------------------------- Add game titles
    steam_multiplayer_games = {x: {"title": multiplayer_titles[x]}
                               for x in range(len(steam_multiplayer_games))}

    # ---------------------------------------- Add game tags
    for x in range(len(multiplayer_tags)):
        upd_dict = {"tags": multiplayer_tags[x]}
        steam_multiplayer_games[x].update(upd_dict)

    # ---------------------------------------- Add game image
    for x in range(len(steam_multiplayer_games)):
        upd_dict = {"image": multiplayer_images[x]}
        steam_multiplayer_games[x].update(upd_dict)

    # ---------------------------------------- Add full game image
    for x in range(len(steam_multiplayer_games)):
        upd_dict = {"full_image": multiplayer_full_images[x]}
        steam_multiplayer_games[x].update(upd_dict)

    # ---------------------------------------- Add game platform tags
    for x in range(len(steam_multiplayer_games)):
        upd_dict = {"pc_platform_tags": multiplayer_platform_tags[x]}
        steam_multiplayer_games[x].update(upd_dict)

    # ---------------------------------------- Add game links
    for x in range(len(steam_multiplayer_games)):
        upd_dict = {"game_link": multiplayer_links[x]}
        steam_multiplayer_games[x].update(upd_dict)


# --------------------------------------------------------------- FAVOURITES

def create_favourites_index():
    global favourites

    game_index = []
    {game_index.append(x) for x in range(len(favourites_game_title))}

    # ---------------------------------------- Add game indices
    for x in range(len(game_index)):
        favourites = dict.fromkeys(game_index, {})


def add_to_favourites_dict():
    global favourites

    # ---------------------------------------- Add game title
    favourites = {x: {"title": favourites_game_title[x]}
                  for x in range(len(favourites))}

    # ---------------------------------------- Add game img
    for x in range(len(favourites)):
        upd_dict = {"image": favourites_game_img[x]}
        favourites[x].update(upd_dict)

    # ---------------------------------------- Add game screenshots
    for x in range(len(favourites)):
        upd_dict = {"screenshots": favourites_game_screenshots[x]}
        favourites[x].update(upd_dict)

    # ---------------------------------------- Add game tags
    for x in range(len(favourites)):
        upd_dict = {"tags": favourites_game_tags[x]}
        favourites[x].update(upd_dict)

    # ---------------------------------------- Add game platform tags
    for x in range(len(favourites)):
        upd_dict = {"pc_platform_tags": favourites_platform_pc[x]}
        favourites[x].update(upd_dict)

    # ---------------------------------------- Add game links
    for x in range(len(favourites)):
        upd_dict = {"game_link": favourite_links[x]}
        favourites[x].update(upd_dict)

    # ---------------------------------------- Add game summary
    for x in range(len(favourites)):
        upd_dict = {"game_summary": favourite_game_summary[x]}
        favourites[x].update(upd_dict)


# -------------------------------------------- Call add to dictionary functions

create_bestsellers_index()
add_to_bestsellers_dict()

create_awardwinners_index()
add_to_awardwinners_dict()

create_action_games_index()
add_to_action_games_dict()

create_adventure_games_index()
add_to_adventure_games_dict()

create_RPG_games_index()
add_to_RPG_games_dict()

create_strategy_games_index()
add_to_strategy_games_dict()

create_multiplayer_games_index()
add_to_multiplayer_games_dict()

create_bestsellers_index()
add_to_bestsellers_dict()

create_favourites_index()
add_to_favourites_dict()
