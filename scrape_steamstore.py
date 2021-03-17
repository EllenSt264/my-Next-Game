"""
** Attribution:

    Splitting elements with BeautifulSoup:
    "https://stackoverflow.com/questions/12616912/split-an-element-with-beautifulsoup"

    Getting href tags with BeautifulSoup:
    "https://stackoverflow.com/questions/43814754/python-beautifulsoup-how-to-get-href-attribute-of-a-element/43814994"

    Looping through a list or URLs with BeautifulSoup:
    "https://stackoverflow.com/questions/44823278/how-to-loop-through-a-list-of-urls-for-web-scraping-with-beautifulsoup"

    Removing duplicate entries within a dictionary:
    "https://stackoverflow.com/questions/4104957/remove-duplicate-entries-from-nested-dictionary-if-two-values-are-the-same-in"

    Fix 'RuntimeError: dictionary changed size during iteration':
    "https://stackoverflow.com/questions/11941817/how-to-avoid-runtimeerror-dictionary-changed-size-during-iteration-error"

    Remove whitespace:
    "https://stackoverflow.com/questions/53424179/beautifulsoup-stripping-whitespace"

    To get past the website's age check:
    "https://stackoverflow.com/questions/33603416/python-beautiful-soup-getting-past-steams-age-check"

"""

import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString

# -------------------------------------------------- Data lists

# -------------- Bestsellers

bs_game_titles = []
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
action_tags = []
action_links = []
action_images = []
action_full_images = []
action_platform_tags = []

# -------------- Adventure Games

adventure_titles = []
adventure_tags = []
adventure_links = []
adventure_images = []
adventure_full_images = []
adventure_platform_tags = []


# -------------- RPG Games

RPG_titles = []
RPG_tags = []
RPG_links = []
RPG_images = []
RPG_full_images = []
RPG_platform_tags = []


# -------------- Strategy Games

strategy_titles = []
strategy_tags = []
strategy_links = []
strategy_images = []
strategy_full_images = []
strategy_platform_tags = []

# -------------- Multiplayer Games

multiplayer_titles = []
multiplayer_tags = []
multiplayer_links = []
multiplayer_images = []
multiplayer_full_images = []
multiplayer_platform_tags = []


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

    for url in url_list:

        cookies = {"birthtime": "786240001", "lastagecheckage": "1-0-1995"}
        source = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(source.text, "html.parser")

        for item in soup.select(".page_content_ctn"):
            if item.find("img", {"class": "package_header"}):
                img = item.select(".package_header")
                for i in img:
                    bs_game_images_full.append(i["src"])

            else:
                img = item.select(".game_header_image_full")
                for i in img:
                    bs_game_images_full.append(i["src"])

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

                    # -------------------------------------------------- Game Links

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


# ----------------------------------------------------------------- GAME GENRES


# ----------------------------------------------------------------- ACTION

def scrape_action_games():
    url = "https://store.steampowered.com/tags/en/Action/#p=0&tab=TopRated"

    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")

    # ---------- Page 1

    for item in soup.select("#TopRatedRows"):
        for a in item.findAll("a", href=True):

            # -------------------------------------------------- Game Titles

            title = a.select(".tab_item_name")
            for i in title:
                title_string = i.string
                action_titles.append(title_string)

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
                action_tags.append(tag)

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

    for url in url_list:

        cookies = {"birthtime": "786240001", "lastagecheckage": "1-0-1995"}
        source = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(source.text, "html.parser")

        for item in soup.select(".page_content_ctn"):
            if item.find("img", {"class": "package_header"}):
                img = item.select(".package_header")
                for i in img:
                    action_full_images.append(i["src"])

            else:
                img = item.select(".game_header_image_full")
                for i in img:
                    action_full_images.append(i["src"])

# ----------------------------------------------------------------- ADVENTURE


def scrape_adventure_games():
    url = "https://store.steampowered.com/tags/en/Adventure/#p=0&tab=TopRated"

    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")

    # ---------- Page 1

    for item in soup.select("#TopRatedRows"):
        for a in item.findAll("a", href=True):

            # -------------------------------------------------- Game Titles

            title = a.select(".tab_item_name")
            for i in title:
                title_string = i.string
                adventure_titles.append(title_string)

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
                adventure_tags.append(tag)

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

    for url in url_list:
        
        cookies = {"birthtime": "786240001", "lastagecheckage": "1-0-1995"}
        source = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(source.text, "html.parser")

        for item in soup.select(".page_content_ctn"):
            if item.find("img", {"class": "package_header"}):
                img = item.select(".package_header")
                for i in img:
                    adventure_full_images.append(i["src"])

            else:
                img = item.select(".game_header_image_full")
                for i in img:
                    adventure_full_images.append(i["src"])
# ----------------------------------------------------------------- RPG


def scrape_RPG_games():
    url = "https://store.steampowered.com/tags/en/RPG/#p=0&tab=TopRated"

    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")

    # ---------- Page 1

    for item in soup.select("#TopRatedRows"):
        for a in item.findAll("a", href=True):

            # -------------------------------------------------- Game Titles

            title = a.select(".tab_item_name")
            for i in title:
                title_string = i.string
                RPG_titles.append(title_string)

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
                RPG_tags.append(tag)

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

    for url in url_list:
        
        cookies = {"birthtime": "786240001", "lastagecheckage": "1-0-1995"}
        source = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(source.text, "html.parser")

        for item in soup.select(".page_content_ctn"):
            if item.find("img", {"class": "package_header"}):
                img = item.select(".package_header")
                for i in img:
                    RPG_full_images.append(i["src"])

            else:
                img = item.select(".game_header_image_full")
                for i in img:
                    RPG_full_images.append(i["src"])

# ----------------------------------------------------------------- STRATEGY


def scrape_strategy_games():
    url = "https://store.steampowered.com/tags/en/Strategy/#p=0&tab=TopRated"

    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")

    # ---------- Page 1

    for item in soup.select("#TopRatedRows"):
        for a in item.findAll("a", href=True):

            # -------------------------------------------------- Game Titles

            title = a.select(".tab_item_name")
            for i in title:
                title_string = i.string
                strategy_titles.append(title_string)

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
                strategy_tags.append(tag)

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

    for url in url_list:
        
        cookies = {"birthtime": "786240001", "lastagecheckage": "1-0-1995"}
        source = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(source.text, "html.parser")

        for item in soup.select(".page_content_ctn"):
            if item.find("img", {"class": "package_header"}):
                img = item.select(".package_header")
                for i in img:
                    strategy_full_images.append(i["src"])

            else:
                img = item.select(".game_header_image_full")
                for i in img:
                    strategy_full_images.append(i["src"])

# ----------------------------------------------------------------- MULTIPLAYER


def scrape_multiplayer_games():
    url = "https://store.steampowered.com/tags/en/Massively%20Multiplayer/#p=0&tab=TopRated"

    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")

    # ---------- Page 1

    for item in soup.select("#TopRatedRows"):
        for a in item.findAll("a", href=True):

            # -------------------------------------------------- Game Titles

            title = a.select(".tab_item_name")
            for i in title:
                title_string = i.string
                multiplayer_titles.append(title_string)

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
                multiplayer_tags.append(tag)

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

    for url in url_list:
        
        cookies = {"birthtime": "786240001", "lastagecheckage": "1-0-1995"}
        source = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(source.text, "html.parser")

        for item in soup.select(".page_content_ctn"):
            if item.find("img", {"class": "package_header"}):
                img = item.select(".package_header")
                for i in img:
                    multiplayer_full_images.append(i["src"])

            else:
                img = item.select(".game_header_image_full")
                for i in img:
                    multiplayer_full_images.append(i["src"])


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

# ------------------------------------------- Dictionaries

steam_bestsellers = {}

steam_award_winners = {}

steam_action_games = {}

steam_adventure_games = {}

steam_RPG_games = {}

steam_strategy_games = {}

steam_multiplayer_games = {}

# ------------------------------------------- Add to dictionaries

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
