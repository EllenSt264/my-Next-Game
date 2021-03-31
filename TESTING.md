# Testing

## Contents

- [Testing User Stories](#testing-user-stories)

    - [First Time User Goals](#first-time-user-goals)

    - [Returning User Goals](#returning-user-goals)


-----

## Testing User Stories 

### First Time User Goals 


1. As a first time user I want to immediately understand the purpose of the application.

2. I want to be able to see an about page or an explanation to what this site is and what it can offer me.


![Website screenshot - Homepage, About Us section](static/img/documentation/screenshot-homepage-about_us.png)

- By scrolling down on the Homepage, users can find a small paragaph that explains a little bit about the site. With this the purpose is made clear.

- The site's title 'My Next Game' clearly defines what type of audience the site is suited for, and can help articulate the site's purpose.


3. I want to be able to find games easily.

![Mockup Image - Homepage](static/img/documentation/screenshot-navbar_genre.png)

![Mockup Image - Games Page](static/img/documentation/screenshot-secondary_navbar.png)

- Users have a vareity of ways in which they can browse the selection of games that are available to them.

- In the navbar, users can select a game genre, using the Genre dropdown menu, to narrow the results when browsing or searching for a game.

- Users have access to secondary navbar, available on all of the game pages (excluding the Favourites page) which allows them to narrow their search further. 

- Users can select a game genre, search for game by using the search bar, or visit a different page entirely, such as the Favourites page or their Profile Game List.

- Users can also browse all available games, if they are not doing so already, by clicking the 'all games' link.


4. I want to be able to use a sort feature so that I only see the results I want.

![Mockup Image - Homepage](static/img/documentation/screenshot-sort.png) 

![Mockup Image - Games Page](static/img/documentation/screenshot-secondary_navbar_short.png)

- The secondary navbar acts a sorting feature, by only displaying game results that match its criteria. For example, clicking the 'Action' button within the Genre Link, will only show games that have the 'Action' game genre tags and/or are primarily categorised as an action game.

- Users can use the searchbar to narrow down their search.


5. I want to be able to register on the site and make a user profile.

![Website screenshot - Register page](static/img/documentation/screenshot-register.png)

- Users can register an account by completing the Register form.


6. I want to see reviews of games, and be able to search for particular game titles or genres of those reviews.

![Mockup Image - Homepage](static/img/documentation/screenshot-review_page-review_cards.png)

![Mockup Image - Games Page](static/img/documentation/screenshot-review_page-with-secondary_navbar.png)

- The Community Reviews page contains all reviews submitted by users.

- The searchbar is available for users to filter these reviews and search for a particular game title.


7. I want to be able to vote on games that I like.

![Mockup Image - Games Page](static/img/documentation/screenshot-like_btn.png)

![Mockup Image - Homepage](static/img/documentation/screenshot-game_card.png) 

- Each game has a like button which allows users to leave likes on games.

- The likes are synchronized acrossed all pages.


8. I want to leave reviews of my own.

![Website screenshot - Register page](static/img/documentation/screenshot-review_form.png)

9. If I don't know what I'm looking for, I want a site feature that will help me decide what game to play next.

- The 'Leave A Review' button on the Community Reviews page allows users to easily leave reviews of their own.

- By filling out a review form, users can submitted their own reviews which will then be displayed on the Community Reviews page.

- Users can only submit one review per game.


10. I want to see games that are recommended by the site.

![Website screenshot - Register page](static/img/documentation/screenshot-homepage-buttons.png)

![Mockup Image - Games Page](static/img/documentation/screenshot-favourites-game_cards.png)

![Mockup Image - Homepage](static/img/documentation/screenshot-favourites-parallax.png) 

![Website screenshot - Register page](static/img/documentation/screenshot-game_cards-recommended.png)

- The Favourites page stores a collection of games that are recommended. These games have been added manually and contain unique content, such as a game summary and screenshots.

- Users can navigate to the Favourites page by clicking on the 'Explore Our Favourites' button on the Homepage or by clicking the 'Our Favourites' navlink in the secondary navbar.

- Any game that is listed within the Favourites page will have a recommended tag ('Recommended By Us') on the game card. 


11. I want to add games to my personal games list.

![Mockup Image - Games Page](static/img/documentation/screenshot-game_cards-add_btn.png)

![Mockup Image - Homepage](static/img/documentation/screenshot-profile-game_list.png) 

- When logged in, a Add Button will be available on each game card for users to click on.

- Once clicked, the selected game will be added to their Profile Game List.

- By default, a game that is added to a user's Profile Game List will be added to the 'Play Later' category, but users can customize this further on their Profile page.


### Returning User Goals

1. As a returning user, I want to be able to customize my profile. I want to add a bio to my profile and upload a custom profile image.

![Mockup Image - Games Page](static/img/documentation/screenshot-profile-sidenav.png)

![Mockup Image - Homepage](static/img/documentation/screenshot-edit_profile.png)

![Mockup Image - Homepage](static/img/documentation/screenshot-edit_profile-avatars.png) 

- After creating an account, users have a the option of customizing their details by clicking on the 'Edit Profile' button on their Profile page.

- On the Edit Profile page, users are able to create a Display Name, edit their email address and add their First and Last name to their Profile.

- On the Edit Profile page, users can navigate to the Avatar page, where they select an Avatar for their profile.

- To make the site more secure, users are required to input their password before any personal details can be changed.

- Each user will be able to see their ID number on the Edit Profile page. This has been included to help implement future security measures. If a user ever needs to contact a site support member about their account, they will be able to provide their ID number to help authenticate their account.


2. I want to be able to see all the reviews that I have made, and have the option to edit or delete them.

![Mockup Image - Homepage](static/img/documentation/screenshot-profile-reviews.png)

![Mockup Image - Homepage](static/img/documentation/screenshot-profile-game_list_2.png)


- Users can see a list of their reviews via their Profile Page, by clicking on the 'Reviews' button in the sidenav.

- On this page, users can review, edit and/or delete any reviews that they have made.

- Additionally, if a user has submitted a review on a game that is currently in their Profile Game List, then a 'Reviewed' button appear in place of the 'Review' button, which will appear if a user has not left a review. Users can click the pen icon besides the 'Reviewed' button to edit their existing review.

- When clicking either the pen icon or the 'Edit' button, users will be directed to the Review form page, with all the current input fields filled in.


3. I want to update my games list. I want to categories games into what I am currently playing, what I have played and want I want to play in the future.

![Mockup Image - Homepage](static/img/documentation/screenshot-profile-game_list-playing.png)

![Mockup Image - Homepage](static/img/documentation/screenshot-profile-game_list-play_later.png)

![Mockup Image - Homepage](static/img/documentation/screenshot-profile-game_list-completed.png)

- Users can update their game list by clicking on the 'Play Later', 'Completed' and/or 'Playing' buttons.

- These buttons will seamlessly move the games to different categories in an easy and intuitive way.

4. I want to see profiles of other users.

5. I want to find the site's contact information so that I can get help on an issue.

6. I want to request new games to be added to the database.

7. I want to add games to a favourites list.

