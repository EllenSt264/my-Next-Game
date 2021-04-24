# Testing

## Contents

- [Automated Testing](#automated-testing)

    - [Page Speed / Performance](#page-performance)

- [Testing User Stories](#testing-user-stories)

    - [First Time User Goals](#first-time-user-goals)

    - [Returning User Goals](#returning-user-goals)


- [Manual Testing](#manual-testing)

    - [Navigation](#navigation)

        - [Navigation - Navbar (Desktop)](#navigation---navbar-desktop)

        - [Navigation - Navbar (Mobile)](#navigation---navbar-mobile)

        - [Navigation - Profile (Mobile)](#navigation---profile-mobile)

        - [Navigation - Profile (Mobile)](#navigation---profile-mobile)

        - [Navigation - Games Page Secondary Navbar (Desktop)](#navigation---games-page-secondary-navbar-desktop)

        - [Navigation - Games Page Secondary Navbar (Mobile)](#navigation---games-page-secondary-navbar-mobile)

        - [Navigation - Other (Desktop)](#navigation---other-desktop)

        - [Navigation - Other (Mobile)](#navigation---other-mobile)

    - [C-R-U-D](#c-r-u-d)

        - [Game Pages, Review Page and Favourites Page](#game-pages-review-page-and-favourites-page)

        - [Profile - Games List](#profile---games-list)

        - [Edit Profile](#edit-profile)

        - [Edit Avatar](#edit-avatar)


- [Bug Fixes](#bug-fixes)

    - [Review Card Collapsible](#review-card-collapsible)

    - [Admin KeyError](#admin-keyerror)

    - [Materialize Tooltip ](#materialize-tooltip)

    - [Edit Profile - Updating Data](#edit-profile---updating-data)

    - [NoneType Error for Request A Game Form](#nonetype-error-for-request-a-game-form)


-----

## Automated Testing

### Page Performance

I used [Google PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/) to measure the speed and performance of my website.


#### Cache Control

Before cache control:

|  Desktop  |  Mobile  |
| --------- | -------- |
| ![Google PageSpeed Insights - before cache control](static/img/documentation/pagespeed-cache_control-desktop-before.png) | ![Google PageSpeed Insights - before cache control](static/img/documentation/pagespeed-cache_control-mobile-before.png) |


After cache control:

|  Desktop  |  Mobile  |
| --------- | -------- |
| ![Google PageSpeed Insights - before cache control](static/img/documentation/pagespeed-cache_control-desktop-after.png) | ![Google PageSpeed Insights - after cache control](static/img/documentation/pagespeed-cache_control-mobile-after.png) |


-----



## Testing User Stories 

### First Time User Goals 


1. As a first time user I want to immediately understand the purpose of the application.

2. I want to be able to see an about page or an explanation to what this site is and what it can offer me.


![Website screenshot - Homepage, About Us section](static/img/documentation/screenshot-homepage-about_us.png)

- By scrolling down on the Homepage, users can find a small paragaph that explains a little bit about the site. With this the purpose is made clear.

- The site's title 'My Next Game' clearly defines what type of audience the site is suited for, and can help articulate the site's purpose.

-----


3. I want to be able to find games easily.

![Screenshot - Navbar](static/img/documentation/screenshot-navbar_genre.png)

![Screenshot - Secondary Navbar on Games page and Reviews page](static/img/documentation/screenshot-secondary_navbar.png)

- Users have a vareity of ways in which they can browse the selection of games that are available to them.

- In the navbar, users can select a game genre, using the Genre dropdown menu, to narrow the results when browsing or searching for a game.

- Users have access to secondary navbar, available on all of the game pages (excluding the Favourites page) which allows them to narrow their search further. 

- Users can select a game genre, search for game by using the search bar, or visit a different page entirely, such as the Favourites page or their Profile Game List.

- Users can also browse all available games, if they are not doing so already, by clicking the 'all games' link.


-----


4. I want to be able to use a sort feature so that I only see the results I want.

![Screenshot - Sort Filter](static/img/documentation/screenshot-sort_filter.png) 

![Screenshot - Secondary Navbar](static/img/documentation/screenshot-secondary_navbar_short.png)

- The secondary navbar acts a sorting feature, by only displaying game results that match its criteria. For example, clicking the 'Action' button within the Genre Link, will only show games that have the 'Action' game genre tags and/or are primarily categorised as an action game.

- Users can use the searchbar to narrow down their search.

- The sort filter allows users to sort the order of the game results on each page. Users can sort the order of games by:

    - Number of Likes

    - Game Title

    - Recommended Games

    - Bestsellers

    - Award Winners

- For each sort filter, users can chose either an ascending or descending order.

-----


5. I want to be able to register on the site and make a user profile.

![Screenshot - Register page](static/img/documentation/screenshot-register.png)

- Users can register an account by completing the Register form.

-----


6. I want to see reviews of games, and be able to search for particular game titles or genres of those reviews.

![Screenshot - Reviews page](static/img/documentation/screenshot-review_page-review_cards.png)

![Screenshot - Secondary Navbar for the Reviews page](static/img/documentation/screenshot-review_page-with-secondary_navbar.png)

- The Community Reviews page contains all reviews submitted by users.

- The searchbar is available for users to filter these reviews and search for a particular game title.

-----


7. I want to be able to vote on games that I like.

![Screenshot - Like button](static/img/documentation/screenshot-like_btn.png)

![Screenshot - game card](static/img/documentation/screenshot-game_card.png) 

- Each game has a like button which allows users to leave likes on games.

- The likes are synchronized acrossed all pages.

-----


8. I want to leave reviews of my own.

![Screenshot - Submit Review form](static/img/documentation/screenshot-review_form.png)

9. If I don't know what I'm looking for, I want a site feature that will help me decide what game to play next.

- The 'Leave A Review' button on the Community Reviews page allows users to easily leave reviews of their own.

- By filling out a review form, users can submitted their own reviews which will then be displayed on the Community Reviews page.

- Users can only submit one review per game.

-----


10. I want to see games that are recommended by the site.

![Screenshot - Homepage buttons](static/img/documentation/screenshot-homepage-buttons.png)

![Screenshot - game cards on the Favourites page](static/img/documentation/screenshot-favourites-game_cards.png)

![Screenshot - Parallax for the Favourites page](static/img/documentation/screenshot-favourites-parallax.png) 

![Screenshot - Recommended tag for the game cards](static/img/documentation/screenshot-game_cards-recommended.png)

- The Favourites page stores a collection of games that are recommended. These games have been added manually and contain unique content, such as a game summary and screenshots.

- Users can navigate to the Favourites page by clicking on the 'Explore Our Favourites' button on the Homepage or by clicking the 'Our Favourites' navlink in the secondary navbar.

- Any game that is listed within the Favourites page will have a recommended tag ('Recommended By Us') on the game card. 

-----


11. I want to add games to my personal games list.

![Screenshot - game cards add button](static/img/documentation/screenshot-game_cards-add_btn.png)

![Screenshot - Profile Game List](static/img/documentation/screenshot-profile-game_list.png) 

- When logged in, an Add Button will be available on each game card for users to click on.

- Once clicked, the selected game will be added to their Profile Game List.

- By default, a game that is added to a user's Profile Game List will be added to the 'Play Later' category, but users can customize this further on their Profile page.

-----


### Returning User Goals

1. As a returning user, I want to be able to customize my profile. I want to add a bio to my profile and upload a custom profile image.

![Screenshot - Profile side nav](static/img/documentation/screenshot-profile-sidenav.png)

![Screenshot - Edit Profile](static/img/documentation/screenshot-edit_profile.png)

![Screenshot - Edit Profile - Avatars](static/img/documentation/screenshot-edit_profile-avatars.png) 

- After creating an account, users have a the option of customizing their details by clicking on the 'Edit Profile' button on their Profile page.

- On the Edit Profile page, users are able to create a Display Name, edit their email address and add their First and Last name to their Profile.

- On the Edit Profile page, users can navigate to the Avatar page, where they select an Avatar for their profile.

- To make the site more secure, users are required to input their password before any personal details can be changed.

- Each user will be able to see their ID number on the Edit Profile page. This has been included to help implement future security measures. If a user ever needs to contact a site support member about their account, they will be able to provide their ID number to help authenticate their account.

-----


2. I want to be able to see all the reviews that I have made, and have the option to edit or delete them.

![Screenshot - Profile Reviews page](static/img/documentation/screenshot-profile-reviews.png)

![Screenshot - Profile Games List](static/img/documentation/screenshot-profile-game_list_2.png)


- Users can see a list of their reviews via their Profile Page, by clicking on the 'Reviews' button in the sidenav.

- On this page, users can review, edit and/or delete any reviews that they have made.

- Additionally, if a user has submitted a review on a game that is currently in their Profile Game List, then a 'Reviewed' button appear in place of the 'Review' button, which will appear if a user has not left a review. Users can click the pen icon besides the 'Reviewed' button to edit their existing review.

- When clicking either the pen icon or the 'Edit' button, users will be directed to the Review form page, with all the current input fields filled in.

-----


3. I want to update my games list. I want to categories games into what I am currently playing, what I have played and want I want to play in the future.

![Screenshot - Profile Games List](static/img/documentation/screenshot-profile-game_list-playing.png)

![Screenshot - Profile Games List](static/img/documentation/screenshot-profile-game_list-play_later.png)

![Screenshot - Profile Games List](static/img/documentation/screenshot-profile-game_list-completed.png)

- Users can update their game list by clicking on the 'Play Later', 'Completed' and/or 'Playing' buttons.

- These buttons will seamlessly move the games to different categories in an easy and intuitive way.

-----

4. I want to see profiles of other users.

![Screenshot - Visit Profile](static/img/documentation/screenshot-visit_profile.png)

- Clicking on the username/display name of a review card on the Community Reviews page, will direct users to the Profile page of that user.

- Users cannot edit profile settings and/or modify the game playlist when visiting another user's Profile.


----

5. I want to find the site's contact information so that I can get help on an issue.


----

6. I want to request new games to be added to the database.

![Screenshot - Request A Game button](static/img/documentation/screenshot-request_game_button_1.png)

![Screenshot - Request A Game button](static/img/documentation/screenshot-request_game_button_2.png)

![Screenshot - Request A Game form](static/img/documentation/screenshot-request_game_form.png)

- Users can navigate to the Request A Game page via the 'Request A Game` buttons on either the Favourites page and/or when no results are available after using the searchbar.

- Once on the Request A Game page, users can then submit a form in order to request games to be added to the database.


-----


7. I want to add games to a favourites list.



-----


## Manual Testing


### Navigation


#### Navigation - Navbar (Desktop)

| No. |   Action    |   Input   |   Expected Output |   Actual Output   |   Result |  Further Comments |
| --- | ----------- | --------- | ----------------- | ----------------- | ---------| ----------------- |
|  1  | Navigate to `Genre` (All Games) page | Click the `Genre` dropdown nav link | The site will navigate to the `Games Page`, listing `all games` within the database | Navigates to `Games Page` and lists `all games` | Pass |
|  2  | Navigate to `Action` Genre page | Click the `Action` nav link within the Genre dropdown menu | The site will navigate to the `Games Page`, listing only the `Action games` within the database | Navigates to `Games Page` and lists all `Action games` | Pass |
|  3  | Navigate to `Adventure` Genre page | Click the `Adventure` nav link within the Genre dropdown menu | The site will navigate to the `Games Page`, listing only the `Adventure games` within the database | Navigates to `Games Page` and lists all `Adventure games` | Pass |
|  4  | Navigate to `RPG` Genre page | Click the `RPG` nav link within the Genre dropdown menu | The site will navigate to the `Games Page`, listing only the `RPG games` within the database | Navigates to `Games Page` and lists all `RPG games` | Pass |
|  5  | Navigate to `Strategy` Genre page | Click the `Strategy` nav link within the Genre dropdown menu | The site will navigate to the `Games Page`, listing only the `Strategy games` within the database | Navigates to `Games Page` and lists all `Strategy games` | Pass |
|  6  | Navigate to `Multiplayer` Genre page | Click the `Multiplayer` nav link within the Genre dropdown menu | The site will navigate to the `Games Page`, listing only the `Multiplayer games` within the database | Navigates to `Games Page` and lists all `Multiplayer games` | Pass |
|  7  | Navigate to `Community Reviews`  page | Click the `Community Reviews` nav link | The site will navigate to the `Community Reviews` page | Navigates to `Community Reviews` page | Pass |
|  8  | Navigate to `Login`  page | Click the `Login` nav link within the `Profile icon` dropdown menu | The site will navigate to the `Login` page | Navigates to `Login` page | Pass |
|  9  | Navigate to `Login`  page | Click the `Login` nav link | The site will navigate to the `Login` page | Navigates to `Login` page | Pass |
|  10  | Navigate to `Login`  page via the Register page | Click the `Log In` link on the Register page | The site will navigate to the `Login` page | Navigates to `Login` page | Pass |
|  11  | `Register` an account | Navigate to the `Register` page and complete the `Register form`; click `Register` | The user will have their account registered and their user credentials will be added to the appropriate MongoDB collection. The user will be directed to their new `Profile` page. A `flash message` should say 'Welcome {username}' | After completing the `register form` the user has their account `registered` and is directed to their `Profile` page. A `flash message` says 'Welcome {username}, which in this case is 'Welcome Firstuser' | Pass |
|  12  | `Log In` | Navigate to the `Login` page and enter credentials; click `Log In` | The user will be `logged in` and directed to their `Profile` page. A `flash message` should say 'Welcome {username}' | After entering user credentials, the user is `'logged in` and directed to their `Profile` page. A `flash message` says 'Welcome {username}, which in this case is 'Welcome Firstuser' | Pass |
|  13  | Navigate to `Profile` page | When logged into an account, hover over the `Profile icon` in the navbar and click on the `Profile` navlink  | The site will navigate to the session user's `Profile` page | Navigates to the session user's `Profile` page | Pass |
|  14  | `Logout` | When logged into an account, hover over the `Profile icon` in the navbar and click on the `Logout` navlink  | The user will be `logged out` and directed to the `Login` page. A `flash message` should say 'You have been logged out' | The user is `logged out` and then directed to the `Login` page. The `flash message` says 'You have been logged out'  | Pass |
|  15  | Navigate to `Homepage` | When on any page other than the Homepage, click the `Home` link in the navbar | The site will navigate to the `Homepage` | Navigates to `Homepage` | Pass |
|  16  | Navigate to `Homepage` | When on any page other than the Homepage, click the `Site Brand Logo` in the navbar | The site will navigate to the `Homepage` | Navigates to `Homepage` | Pass |
|  17  | Navigate to a `Games Page` with `browser cookies cleared` | Clear browser `cookies` and reload the site. Click the `Genre` navlink to navigate to the `Games Page` for all games | Should navigate to the `Games Page` for all games | KeyError for `navSelect1` and `navSelect2` occurs; page does not load | Fail | See fix [here](#navselect-keyerror) |
|  17  | Navigate to a `Games Page` with `browser cookies cleared` after fix | Clear browser `cookies` and reload the site. Click the `Genre` navlink to navigate to the `Games Page` for all games | Should navigate to the `Games Page` for all games | Navigates to `Games Page` | Pass |


#### Navigation - Navbar (Mobile)

| No. |   Action    |   Input   |   Expected Output |   Actual Output   |   Result |  Further Comments |
| --- | ----------- | --------- | ----------------- | ----------------- | ---------| ----------------- |
|  1  | Trigger Mobile Sidenav | Using `Chrome DevTools`, toggle device toolbar and change the viewport to a tablet or mobile device with a max width of 992px | The `Home`, `Platform`, `Genre` and `Community Reviews` nav links should disappear. A `hamburger icon` should appear to the right in the their place. When clicked it should trigger the mobile `sidenav` | The navbar collapses at 992px; the `Home`, `Platform`, `Genre` and `Community Reviews`  nav links disappear and in its place is the `hamburger icon`, which opens the `side nav` once clicked | Pass |
|  2  | Navigate to `Genre` (All Games) page | Click the `Genre` nav link inside the mobile `sidenav` | The site will navigate to the `Games Page`, listing `all games` within the database | Navigates to `Games Page` and lists `all games` | Pass |
|  3  | Navigate to `Action` Genre page | Click the `Action` nav link inside the mobile `side nav` | The site will navigate to the `Games Page`, listing only the `Action games` within the database | Navigates to `Games Page` and lists all `Action games` | Pass |
|  4  | Navigate to `Adventure` Genre page | Click the `Adventure` nav link inside the mobile `side nav` | The site will navigate to the `Games Page`, listing only the `Adventure games` within the database | Navigates to `Games Page` and lists all `Adventure games` | Pass |
|  5  | Navigate to `RPG` Genre page | Click the `RPG` nav link inside the mobile `side nav` | The site will navigate to the `Games Page`, listing only the `RPG games` within the database | Navigates to `Games Page` and lists all `RPG games` | Pass |
|  6  | Navigate to `Strategy` Genre page | Click the `Strategy` nav link inside the mobile `side nav` | The site will navigate to the `Games Page`, listing only the `Strategy games` within the database | Navigates to `Games Page` and lists all `Strategy games` | Pass |
|  7  | Navigate to `Multiplayer` Genre page | Click the `Multiplayer` nav link inside the mobile `side nav` | The site will navigate to the `Games Page`, listing only the `Multiplayer games` within the database | Navigates to `Games Page` and lists all `Multiplayer games` | Pass |
|  8  | Navigate to `Community Reviews`  page | Click the `Community Reviews` nav link inside the mobile `side nav` | The site will navigate to the `Community Reviews` page | Navigates to `Community Reviews` page | Pass | **Bug:** Once directed to the `Community Reviews` page, all nav links other than the Site Brand logo disappears. **Fix:** Adding `overflow: hidden` to the HTML tag seems to fix the issue |
|  9  | Trigger `Profile` mobile `sidenav` | Click on the `Profile icon` in the navbar | It should trigger a `sidenav`, to the left, which contains either the `Login` and `Register` navlink, or the `Profile` and `Log Out` navlink | The `sidenav` triggers, opening to the left, once the `Profile icon` is clicked | Pass |
|  10  | Navigate to `Login`  page | Click the `Login` nav link within the `Profile sidenav` | The site will navigate to the `Login` page | Navigates to `Login` page | Pass |
|  11  | Navigate to `Register`  page | Click the `Register` nav link within the `Profile sidenav` | The site will navigate to the `Register` page | Navigates to `Register` page | Pass |
|  12  | Navigate to `Homepage` | When on any page other than the Homepage, click the `Site Brand Logo` in the navbar | The site will navigate to the `Homepage` | Navigates to `Homepage` | Pass |
|  13  | Navigate to `Profile` page | When logged into an account, click the `Profile` navlink within the `Profile sidenav` | The site will navigate to the session user's `Profile` page | Navigates to the session user's `Profile` page | Pass |
|  14  | Logout | When logged into an account, click the `Logout` navlink within the `Profile sidenav` | The user will be `logged out` and directed to the `Login` page. A `flash message` should say 'You have been logged out' | The user is `logged out` and then directed to the `Login` page. The `flash message` says 'You have been logged out'  | Pass |


#### Navigation - Profile (Desktop)

| No. |   Action    |   Input   |   Expected Output |   Actual Output   |   Result |  Further Comments |
| --- | ----------- | --------- | ----------------- | ----------------- | ---------| ----------------- |
|  1  | Navigate to `Profile - Reviews` page | When on the `Profile` page, click the `Reviews` button in the sidenav - to the right | It should direct to the `Profile - Reviews` page | Directs to `Profile - Reviews` page | Pass |
|  2  | Navigate to `Profile - Games` page (default page for the Profile) | While still on the `Profile - Reviews` page, click the `Games` button in the sidenav | Direct to the `Profile - Games` page (the default page whenever the `Profile` navlink is clicked) | Directs to `Profile - Games` page | Pass |  
|  3  | Navigate to `Edit Profile` page | When on the `Profile` page, click the `Edit Profile` button in the sidenav | Direct to `Edit Profile` page | Directs to `Edit Profile` page | Pass |  
|  4  | Navigate to `Edit Profile - Avatar` page | While still on the `Edit Profile` page, click the `Avatar` button in the sidenav | It should direct to `Edit Profile - Avatar` page | Directs to `Edit Profile - Avatar` page | Pass |  
|  5  | Navigate to `Edit Profile - General` page (default page for Edit Profile) | While still on the `Edit Profile - Avatar` page, click the `General` button in the sidenav | It should direct to `Edit Profile - General` page (default page for Edit Profile) | Directs to `Edit Profile - General` page | Pass |
|  6  | Navigate to `Edit Profile - General` page (2) | While on the `Edit Profile - Avatar` page, click the `Edit Profile` link heading at the top of the card | It should direct to `Edit Profile - General` page | Directs to `Edit Profile - General` page | Pass |
|  7  | Navigate back to `Profile` page | While on any of the `Edit Profile` pages, click the `username` link heading at the top of the card | It should direct back to the `Profile - Games` page | Directs to `Profile - Games` page | Pass |   


#### Navigation - Profile (Mobile)

| No. |   Action    |   Input   |   Expected Output |   Actual Output   |   Result |  Further Comments |
| --- | ----------- | --------- | ----------------- | ----------------- | ---------| ----------------- |
|  1  | Navigate to `Profile - Reviews` page | When on the `Profile` page, click the `Reviews` button | It should direct to the `Profile - Reviews` page | Directs to `Profile - Reviews` page | Pass |
|  2  | Navigate to `Profile - Games` page (default page for the Profile) | While still on the `Profile - Reviews` page, click the `Games` button | Direct to the `Profile - Games` page (the default page whenever the `Profile` navlink is clicked) | Directs to `Profile - Games` page | Pass |  
|  3  | Navigate to `Edit Profile` page | When on the `Profile` page, click the `Edit Profile` button | Direct to `Edit Profile` page | Directs to `Edit Profile` page | Pass |  
|  4  | Navigate to `Edit Profile - Avatar` page | While still on the `Edit Profile` page, click the `Avatar` button | It should direct to `Edit Profile - Avatar` page | Directs to `Edit Profile - Avatar` page | Pass |  
|  5  | Navigate to `Edit Profile - General` page (default page for Edit Profile) | While still on the `Edit Profile - Avatar` page, click the `General` button | It should direct to `Edit Profile - General` page (default page for Edit Profile) | Directs to `Edit Profile - General` page | Pass |
|  6  | Navigate to `Edit Profile - General` page (2) | While on the `Edit Profile - Avatar` page, click the `Edit Profile` link heading at the top of the card | It should direct to `Edit Profile - General` page | Directs to `Edit Profile - General` page | Pass |
|  7  | Navigate back to `Profile` page | While on any of the `Edit Profile` pages, click the `username` link heading at the top of the card | It should direct back to the `Profile - Games` page | Directs to `Profile - Games` page | Pass |
|  8  | Navigate back to `Profile` page (2) | While on any of the `Edit Profile` pages, click the `Back to Profile` link below the heading | It should direct back to the `Profile - Games` page | Directs to `Profile - Games` page | Pass |      


#### Navigation - Games Page Secondary Navbar (Desktop)

| No. |   Action    |   Input   |   Expected Output |   Actual Output   |   Result |  Further Comments |
| --- | ----------- | --------- | ----------------- | ----------------- | ---------| ----------------- |
|  1  | Navigate to `Favourites` page | Click the `Genre` navlink in the navbar to navigate to the `Games` page, displaying **all games** in the database. Once there, click the `Our Favourites` navlink in the `secondary navbar` | It should direct to the `Favourites` page | Directs to `Favourites` page | Pass |
|  2  | Show Genre tags | Click the `Genre` link in the `secondary navbar` | It should display all of the genre links (`Action`, `Adventure`, `RPG`, `Strategy` and `Multiplayer`) and the `Genre` link should no longer be visible | Displays all genre links. The `Genre` link itself is no longer visible | Pass |
|  3  | Show Platform tags | Click the `Platform` link in the `secondary navbar` | It should display all of the platform links (`PC`, `XBOX` and `Playstation`) and the `Platform` link should no longer be visible | Displays all platform links. The `Platform` link itself is no longer visible | Pass |
|  4  | Navigate to a user's `Profile - Game List` | When `logged in`, click the `Your List` navlink in the `secondary navbar` | It should direct to the user to their `Profile - Game List` | Directs to the user to their `Profile - Game List` | Pass |
|  5  | Search for a game title using the `searchbar` in the `secondary navbar` | Input 'Red' into the `searchbar` and hit enter | The page should display two game results: 'Red Dead Online' and 'Red Dead Redemption 2' | After searching for 'red', the page displays the two game results containing that name: 'Red Dead Online' and 'Red Dead Redemption 2' | Pass |
|  6  | Display all games in the database | Hover over the `Genre` dropdown menu (navlink) and click on the `Action` navlink in the navbar to navigate to the `Games - Action` page. Click on the `All Games` link in the `secondary navbar` once there | After the clicking the link, all games should be displayed on the page | Before clicking the link there were 12 pages, containing games that had the 'Action' tag and/or were primarily categorised as 'Action' (for more information on how the data is handled, see [here]()). After clicking `All Games`, there were 18 pages, containing all games within the database | Pass |


#### Navigation - Games Page Secondary Navbar (Mobile)

| No. |   Action    |   Input   |   Expected Output |   Actual Output   |   Result |  Further Comments |
| --- | ----------- | --------- | ----------------- | ----------------- | ---------| ----------------- |
|  1  | Navigate to `Favourites` page | Click the `Genre` navlink in the main `sidenav` to navigate to the `Games` page, displaying **all games** in the database. Once there, click on the `hamburger icon` in the `secondary navbar`. Then click the `Our Favourites` navlink in the `secondary navbar sidenav` | It should direct the user to the `Favourites` page | Directs the user to `Favourites` page | Pass |
|  2  | Navigate to a user's `Profile - Game List` | When `logged in`, click the `Your List` navlink in the `secondary navbar sidenav` | It should direct to the user to their `Profile - Game List` | Directs to the user to their `Profile - Game List` | Pass |
|  5  | Search for a game title using the `searchbar` in the `secondary navbar` | Input 'Red' into the `searchbar` and hit enter | The page should display two game results: 'Red Dead Online' and 'Red Dead Redemption 2' | After searching for 'red', the page displays the two game results containing that name: 'Red Dead Online' and 'Red Dead Redemption 2' | Pass |
|  6  | Display all games in the database | Hover over the `Genre` dropdown menu (navlink) and click on the `Action` navlink in the navbar to navigate to the `Games - Action` page. Click on the `All Games` link in the `secondary navbar` once there | After the clicking the link, all games should be displayed on the page | Before clicking the link there were 12 pages, containing games that had the 'Action' tag and/or were primarily categorised as 'Action' (for more information on how the data is handled, see [here]()). After clicking `All Games`, there were 18 pages, containing all games within the database | Pass |


#### Navigation - Other (Desktop)

| No. |   Action    |   Input   |   Expected Output |   Actual Output   |   Result |  Further Comments |
| --- | ----------- | --------- | ----------------- | ----------------- | ---------| ----------------- |
|  1  | Navigate to `Favourites` page | When on the `Homepage`, click the `Explore Our Favourites` button | It should direct to the `Favourites` page | Directs to `Favourites` page | Pass |
|  2  | Navigate to `Favourites` page | When on any of the `Game` pages, click the `Our Favourites` navlink in the `secondary navbar` | It should direct to the `Favourites` page | Directs to `Favourites` page | Pass |
|  3  | Navigate to `Submit Review` page | When on the`Community Reviews` page, click the `Leave a Review` button | It should direct to the `Submit Review` page | Directs to `Submit Review` page | Pass |
|  4  | Navigate to `Submit Review` page from the `Profile` page | When on the session user's`Profile` page, find a game within any section of the `Games List` (if none have been added then see [here]() to add some) that has not yet been reviewed by the user. Click the `Review` button beside it | Should direct the user to the `Submit Review` page and the game title should **already be filled in** with the game from the user's `Game List` | Directs to the `Submit Review` page. The correct game title for the *game title*  `input field` is already filled in | Pass |
|  5  | Navigate to `Edit Review` page from the `Profile` page | When on the session user's`Profile` page, find a game within any section of the `Games List` (if none have been added then see [here]() to add some) that **have** been reviewed by the user. If no reviews have been made yet, then see [here]() to submit one. Click the `pen icon` inside the `Reviewed` button | Should direct the user to the `Edit Review` page and all `input fields` should **already be filled in** with the data from the current review that the user wishes to edit | Directs the user to the `Edit Review` page. All `input fields` are filled in with data from the review that the user wishes to edit | Pass |
|  5  | Navigate to `Edit Review` page from the `Profile - Reviews` page | When on the session user's`Profile - Reviews` page, find any review within the list (no reviews have been made yet, then see [here]() to submit one). Click the `Edit` button inside the review card | Should direct the user to the `Edit Review` page and all `input fields` should **already be filled in** with the data from the current review that the user wishes to edit | Directs the user to the `Edit Review` page. All `input fields` are filled in with data from the review that the user wishes to edit | Pass |


#### Navigation - Other (Mobile)

| No. |   Action    |   Input   |   Expected Output |   Actual Output   |   Result |  Further Comments |
| --- | ----------- | --------- | ----------------- | ----------------- | ---------| ----------------- |
|  1  | Navigate to `Favourites` page | When on the `Homepage`, click the `Explore Our Favourites` button | It should direct to the `Favourites` page | Directs to `Favourites` page | Pass |
|  2  | Navigate to `Favourites` page | When on any of the `Game` pages, click the `hamburger icon` in th the `secondary navbar`, then click the `Our Favourites` navlink in the `sidenav` | It should direct to the `Favourites` page | Directs to `Favourites` page | Pass |
|  3  | Navigate to `Submit Review` page | When on the`Community Reviews` page, click the `Leave a Review` button | It should direct to the `Submit Review` page | Directs to `Submit Review` page | Pass |
|  4  | Navigate to `Submit Review` page from the `Profile` page | When on the session user's`Profile` page, find a game within any section of the `Games List` (if none have been added then see [here]() to add some) that has not yet been reviewed by the user. Click the `Review` button beside it | Should direct the user to the `Submit Review` page and the game title should **already be filled in** with the game from the user's `Game List` | Directs to the `Submit Review` page. The correct game title for the *game title*  `input field` is already filled in | Pass |
|  5  | Navigate to `Edit Review` page from the `Profile` page | When on the session user's`Profile` page, find a game within any section of the `Games List` (if none have been added then see [here]() to add some) that **have** been reviewed by the user. If no reviews have been made yet, then see [here]() to submit one. Click the `pen icon` inside the `Reviewed` button | Should direct the user to the `Edit Review` page and all `input fields` should **already be filled in** with the data from the current review that the user wishes to edit | Directs the user to the `Edit Review` page. All `input fields` are filled in with data from the review that the user wishes to edit | Pass |
|  6  | Navigate to `Edit Review` page from the `Profile - Reviews` page | When on the session user's`Profile - Reviews` page, find any review within the list (no reviews have been made yet, then see [here]() to submit one). Click the `Edit` button inside the review card | Should direct the user to the `Edit Review` page and all `input fields` should **already be filled in** with the data from the current review that the user wishes to edit | Directs the user to the `Edit Review` page. All `input fields` are filled in with data from the review that the user wishes to edit | Pass |


------

### C-R-U-D


#### Game Pages, Review Page and Favourites Page

| No. |   Action    |   Input   |   Expected Output |   Actual Output   |   Result |  Further Comments |
| --- | ----------- | --------- | ----------------- | ----------------- | ---------| ----------------- |
|  1  | `Like` a game when **not** logged in | Click any game card's `like button` on the `Games` page. Ensure you are **not** logged in | A `tooltip` should trigger, and no like should be added | Once clicking on the `like button` a `tooltip` is triggered above it, saying 'Please sign in or register an account with us to leave likes on games' | Pass |
|  2  | **Sign in** and `Like` a game | Click any game card's `like button` on the `Games` page. Ensure you **are** logged in and like a game that you **have not** liked before | Your like should be added to the database and a `flash message` should appear notifying you that your like was successful. The `like count` on the game card should increment by 1 | After clicking the `like button` a `flash message` appears, saying 'Liked added!'. The `like count` is incremented by 1 | Pass |
|  3  | `Add a game` to a user's `Game List` | When logged in, click any game card's floating `add button` on the `Games` page. Click on a game that **does not** already exisit in your `Games List` | A `flash message` should notify you that your action was successful and the game should be added to the 'Play Later' section of your `Games List`. Visit the `Profile` page to check | A `flash message` says 'Game Successfully Added to List' and the game is added to the 'Play Later' section of the `Games List` | Pass | The floating `add button` does **not** show when a user is **not** logged in, as intended |
|  4  | `Add a game` to a user's `Game List` that **already exisits** | When logged in, click a game card's floating `add button` on the `Games` page. Ensure that the game you pick **already exisits** in your `Games List` | A `flash message` should notify you that your action was **not** successful because the game already exisits in your `Games List`. If you were to go on the `Profile - Games List` page, only **one copy** of the game should be present | A `flash message` says 'You've Already Added This Game'. The game was **not** added again to the `Games List` | Pass | The floating `add button` is **only** visible when a user **is** logged in, as intended |
|  5  | `Submit Review` when **not** logged in | Navigate to `Community Reviews` page and click the `Leave A Review` button. Ensure you are **not** logged in | A `tooltip` should trigger telling the user to log in first | Triggers a `tooltip` that says 'Please sign in or register an account with us to submit reviews' | Pass |
|  6  | **Log in** and `Submit Review` | Navigate to `Community Reviews` page and click the `Leave Review` button. Fill out **all** required fields and click submit | It should submit your review and redirect you to the `Community Reviews` page | Successfully submits review. Redirects to the `Community Reviews` page and triggers a `flash message` that says 'Review Successfully Submitted'. Upon scrolling down the new review can be seen within the review results and all details are correct | Pass |
|  7  | **Log in** and `Submit Review` via the `Profile page` | Navigate to the user's `Profile` page, ensuring that a game has been added to the user's `Game List`, and locate a game to review. Click the `Review` button within the game card. Submit a review | Clicking the `Review` button should direct the user to the `Submit Review` page. The game title should be already filled in with the game title from the user's `Game List`. Filling out all required fields should submit the review and redirect the user to the `Community Reviews` page | Upon clicking the `Review` button, I am directed to the `Submit Review` page, with the correct game title already filled in. Successfully submits review once all required fields are filled. Redirects to the `Community Reviews` page and triggers a `flash message` that says 'Review Successfully Submitted'. Upon scrolling down the new review can be seen within the review results and all details are correct | Pass |
|  8  | **Log in** and `Submit Review` that the user has **already submitted** | Navigate to `Community Reviews` page and click the `Leave Review` button. Pick a game from the game title select field that the user has **already** reviewed. Fill out **all** required fields and click submit | It should **not** submit your review but still redirect you to the `Community Reviews` page | As intended, it does **not** submit the review. Redirects to the `Community Reviews` page and triggers a `flash message` that says 'You've Already Submitted a Review for this Game' | Pass |
|  9  | `Update Review` | While **logged in**, navigate to the `Profile - Reviews` page and find a review you want to update. Click the `Edit` button | It should navigate to the `Edit Review` page and all fields should be filled in with the data from your existing review. Edit one or several fields and submit | It should update your review and redirect you to the `Community Reviews` page | Successfully updates review. Redirects to the `Community Reviews` page and triggers a `flash message` that says 'Review Successfully Updated'. Upon scrolling down the new review can be seen within the review results and all details are correct | Pass |
|  10  | `Delete Review` - modal | While **logged in**, navigate to the `Profile - Reviews` page and find a review you want to delete. Click the `Delete` button | It should trigger a `modal` | Triggers a modal asking if I am sure if I want to proceed with my action | Pass |
|  11  | `Delete Review` | While **logged in**, navigate to the `Profile - Reviews` page and find a review you want to delete. Click the `Delete` button and click `Yes, Delete` in the modal | It should delete the review | Successfully deletes the review and triggers a `flash message` that says 'Review Successfully Deleted'. The review is no longer in my reviews list on the `Profile - Reviews` page | Pass |
|  12  | `Request A Game` when **not** logged in | Navigate to `Favourites` page and scroll down until you see the `Request A Game` button. Click it when you are **not** logged in | A `tooltip` should trigger telling the user to log in first | Triggers a `tooltip` that says 'Please sign in or register an account with us to request games' | Pass |
|  12  | `Request A Game` | Navigate to `Favourites` page and scroll down until you see the `Request A Game` button. Click it, ensuring that you **are** logged in. Request a game to be added to the database | It should navigate to the `Request A Game` page. After filling in all required fields it should redirect to the Homepage with your request submitted | It successfully navigates to the `Request A Game` page but submitting the form triggers a `TypeError` | Fail | See fix [here](#nonetype-error-for-request-a-game-form) |
|  13  |  `Request A Game` - attempt 2 | Navigate to `Favourites` page and scroll down until you see the `Request A Game` button. Click it, ensuring that you **are** logged in. Request a game to be added to the database | It should navigate to the `Request A Game` page. After filling in all required fields it should redirect to the Homepage with your request submitted | After navigating to the `Request A Game` page, and completing the form input fields, the game request is submitted successfully. A `flash message` says 'Your Request Has Been Submitted` | Pass |
|  14  | Request the **same** game via the `Request A Game` page | On the `Request A Game` page, fill in the form fields and request the **same** game as before. Ensure that the **same** user is still logged in | The request should not be successful and the page should reload | The game request is **not** submitted and the page reloads as intended. A `flash message` triggers, which says 'You've already submitted a request for this game' | Pass |
|  15  | Request the **same** game as a **different user** | Log in as a **different user** and follow the same steps as above in order to request the same game as before via the `Request A Game` page | The request should be submitted, but it should **update** an existing document in the database rather than create a new one | The request is submitted successfully. The user is redirected to the Homepage and a `flash message` says 'Your Request Has Been Submitted' which confirms that the user's actions were successful. The database has updated an existing document by appending the username of the session user to the `requested_by` array | Pass | For more details on the database schema, see [here]() |
|  16  | Do everything above but on a mobile device | n/a | n/a | n/a | Pass |


#### Profile - Games List

| No. |   Action    |   Input   |   Expected Output |   Actual Output   |   Result |  Further Comments |
| --- | ----------- | --------- | ----------------- | ----------------- | ---------| ----------------- |
|  1  | `Move` a game to the 'Currently Playing' section of the `Games List` | Ensure there are multiple games within the `Profile - Game List` to work with. From either the 'Play Later' section or the 'Completed' section, click the `playing` button next to a game | The game should move to the 'Currently Playing' section and a flash message should notify you that your action was succesful | Game moved to the 'Currently Playing' section once the `playing` button was clicked. The `flash message` said 'Game Successfully Moved to Playing' | Pass |
|  2  | `Move` a game to the 'Play Later' section of the `Games List` | Ensure there are multiple games within the `Profile - Game List` to work with. From either the 'Playing' section or the 'Completed' section, click the `play later` button next to a game | The game should move to the 'Play Later' section and a flash message should notify you that your action was succesful | Game moved to the 'Play Later' section once the `play later` button was clicked. The `flash message` said 'Game Successfully Moved to Play Later' | Pass |
|  3  | `Move` a game to the 'Completed' section of the `Games List` | Ensure there are multiple games within the `Profile - Game List` to work with. From either the 'Playing' section or the 'Play Later' section, click the `completed` button next to a game | The game should move to the 'Completed' section and a flash message should notify you that your action was succesful | Game moved to the 'Completed' section once the `completed` button was clicked. The `flash message` said 'Game Successfully Moved to Completed' | Pass |
|  4  | `Remove` a game from the `Games List` - trigger `modal` | Click on the `remove game` button next to a game | A `modal` should trigger asking you to check if want to remove the game | The `modal` trigger once the button is clicked | Pass |
|  5  |`Remove` a game from the `Games List` - cancel | Click on the `remove game` to trigger the `modal` then click the `cancel` button | The `modal` should close, and the game should still be in the `Games List`. No game should be deleted | The `modal` closes and the game is still there - no game has been removed from the `Games List` | Pass |
|  6  | `Remove` a game from the `Games List` | Click on the `remove game` to trigger the `modal` then click the `yes, delete` button | The `modal` should close, having removed the game from the `Games List`. A `flash message` should notify you that your action was successful | After clicking `yes, delete` in the `modal`, the `modal` closes and a `flash message` says 'Game Successfully Removed from Your List'. The game has been **removed** from the `Games List` | Pass |


#### Edit Profile

| No. |   Action    |   Input   |   Expected Output |   Actual Output   |   Result |  Further Comments |
| --- | ----------- | --------- | ----------------- | ----------------- | ---------| ----------------- |
|  1  | Update `Display Name` - cancel | On the `Edit Profile - General` page, click on the `edit` button beside the `display name input field` and create a display name for your user. Click `cancel` once done | All `input fields` should refresh | Upon clicking `cancel` all `input fields` refresh | Pass | This works correctly for each `input field` on this page |
|  2  | Update `Display Name` - verification | On the `Edit Profile - General` page, click on the `edit` button beside the `display name input field` and create a display name for your user. Click `save changes` once done | Clicking `save changes` should trigger a `modal`, asking for you to input your `password` in order to update your account details | Clicking `save changes` triggers the `modal` which asks for `password verification` | Pass |
|  3  | Update `Display Name` | On the `modal`, enter the user's password and click `save changes` | The `Display Name` should be updated and a flash message should notify you that your actions were successful | The `Display Name` successfully update and the `flash message` was trigger, saying 'Profile Setting Successfully Updated' | Pass |
|  4  | Trying the same thing with differerent `input fields` produced the same result and worked as intended | n/a | n/a | n/a | Pass |
|  5  | Update `avatar` | Navigate to `Edit Profile - Avatar` and click on any avatar image below the 'Available Avatars' heading | Your `avatar` should be updated and a `flash message` should notify you that the action was successful | The `avatar` image updates and the `flash message` states 'Avatar Successfully Updated' | Pass |



#### Admin Controls 

| No. |   Action    |   Input   |   Expected Output |   Actual Output   |   Result |  Further Comments |
| --- | ----------- | --------- | ----------------- | ----------------- | ---------| ----------------- |
|  1  | Check if `Admin Controls` navlink is present | Log in as an admin user | `Admin Controls` navlink should be visible in the navbar | `Admin Controls` is present in the navbar | Pass |
|  2  | See `User Requests` | Via the `Admin Controls` dropdown (or side nav if on mobile) navigate to `User Requests` | A list of all user game requests submitted via the `Request A Game` page should be visible. It should match the `game_requests` collection in the database | The page displays a list of all users game requests that match the data in the `game_requests` collection | Pass | 
|  3  | `Add To DB Queue` | Navigate to `Add Game To DB` page and fill in all required fields. Take a game link from the [Steam Store]() page and paste the URL for that game page into the game page url form input. Ensure that the game does **not** already exist in the db (using the search filter on a game page to check). Submit the form | It should add the game link and its chosen category, or categories, to the `admin_game_links` collection | I filled in all required fields, and added the game URL for 'Mortal Kombat 11'. The form was successfully submitted, which triggered the `flash message` 'Successfully Added Data'. The new data was successfully added to the `admin_game_links` collection in the db | Pass |
|  4  | `Update DB` | Navigate to the `Update DB` page and input the admin user's password. Click the update button | It should update the database by first checking if a game link from `admin_game_links` already exists in the `all_pc_games` collection. If it doesn't already exist then it should run program to scrape data from the game link provided from `admin_game_links` and then add that data to `all_pc_games`. Any new games should now be added to the site | The database was **not** updated, instead submitting the form triggered the `flash message` 'Database Already Updated' and I was redirected back to the Homepage | Fail | 
|  5  | `Update DB` - attempt 2 | Same as above | Same as above | After altering the code I tried updating the database again. This time it was successfully and a `flash message` said 'Successfully Updated Database'. I checked this by navigating to a `Games` page and searching for 'Mortal' in the searchbar. It then showed the result for 'Mortal Kombat 11' with all the correct data, meaning the database was indeed updated. I then checked if any existing data within the `admin_game_links` had been added **again**, which would mean duplicate data. I searched for 'Ash Of Gods Redemption', which had already been added to the `all_pc_games` collection. Only one copy of the game exists meaning no duplicate data was created | Pass | This bug was caused by an identation error with the following code: `if not existing_game: mongo.db.all_pc_games.insert_one(game)`. Fixing the indentation corrected this issue |


-----

## Bug Fixes

### Review Card Collapsible

- When making the review cards on the Community Reviews page, I used the Materialize collapsible to store larger content. However, when clicking the collapsible header the following bug occurred:

![Review card collapsible visual bug](static/img/documentation/bug-review_collapsible.gif)

I narrowed the cause of bug down to how the rows and collumns were handled with Jinja:

```
<div class="row" id="reviewCards">
    {% for review in game_reviews %}
        {% if loop.index0 % 3 == 0 %}
            <!-- Review card -->
            <div class="col s12 m6 l4 left-review-card review-card" id="left-review-card">
                .....
            </div>
        {% else %}
            <!-- Review card -->
            <div class="col s12 m6 l4 left-review-card review-card" id="left-review-card">
                .....
            </div>
        {% endif %}
    {% endfor %}
</div>
```

To fix this bug I created a new 'row' div for every third iteration of the loop index. Then, to ensure that the cards were centered as before, I added the 'left-review-card' id variable with Jinja, with help from [this source](https://stackoverflow.com/questions/43858134/how-to-add-conditional-css-class-based-on-python-if-statement)


```
<div class="row" id="reviewCards">
    {% for review in game_reviews %}
        {% if loop.index % 3 != 0 %}
            <!-- Review card -->
            <div class="col s12 m6 l4 review-card" id="{{ 'left-review-card' if loop.index0 % 3 == 0 }}">
                .....
            </div>
        {% else %}
            <div class="row">
                <!-- Review card -->
                <div class="col s12 m6 l4 review-card">
                    .....
                </div>
            </div>
        {% endif %}
    {% endfor %}
</div>
```


This is how the collapsible looks after fixing the bug:

![Review card collapsible after fix](static/img/documentation/fix-review_collapsible.gif) 


-----


### Admin KeyError

- The following code in `app.py` was causing a "KeyError: 'user'" error in the browser when no user was logged into the site:

`admin = mongo.db.user.find_one({"username": session["user"]})["admin"]`

- To fix this, I replaced the admin variable with a new session cookie, which is created upon logging in:

```
# Create session cookie for admin
user = mongo.db.users.find_one({
    "username": request.form.get("username").lower()})
admin = user["admin"]

if admin is True:
    session["admin"] = True
else:
    session["admin"] = False
```

The session cookie can be seen in the Network tab of Chrome DevTools:

|  Admin = False  |  Admin = True  |
| --------------- | -------------- |
| ![Screenshot of admin session cookie, false](static/img/documentation/screenshot-session_admin-false.png) | ![Screenshot of admin session cookie, true](static/img/documentation/screenshot-session_admin-true.png)

No errors were produced; fixing this issue.


-----


### NavSelect KeyError

- Navigating to any of the Game pages with the browser cookies cleared, would trigger a "KeyError: 'navSelect1'" error in the browser. This was caused by session cookie not being defined properly. The following code caused the issue:

```
if request.method == "POST":
    session["navSelect1"] = request.form.get("navSelect1").lower()
    session["navSelect2"] = request.form.get("navSelect2").lower()
```

- There was nothing in place to define the session cookie for when the sort filter form is not in use. I.e, when running the website for the first time and navigating to any of the Games pages. 

- Add the following code to the conditional statement fixed the error:

```
if request.method == "POST":
        session["navSelect1"] = request.form.get("navSelect1").lower()
        session["navSelect2"] = request.form.get("navSelect2").lower()
    else:
        session["navSelect1"] = "default"
        session["navSelect2"] = "desc"
```


-----

### Materialize Tooltip 

- Materialize tooltip was not working due to a conflict between Materialize and JQuery-UI. 

- To fix this I had to build a custom JQuery-UI JS file and JQuery-UI Themes CSS file with [JQuery Download Builder](https://jqueryui.com/download/) and replace the standard CDN link.


-----

## Edit Profile - Updating Data

- When attempting to update user data on the Edit Profile page, any fields that were not filled again by the user were updating to `null` rather than keeping their default values.

- This was caused by the 'disabled` attribute in the HTML code. To fix this, I created some custom JS code to remove the disable attribute from the input fields once the 'submit' button is clicked. This allowed me to keep the function of the disabled attribute but prevent any null errors from happening, as the disabled attribute is removed before the database is updated.

```
$('#saveChanges').on('click', function() {
    $('#edit-displayName').prop('disabled', false);
    $('#edit-email').prop('disabled', false);
    $('#edit-fname').prop('disabled', false);
    $('#edit-lname').prop('disabled', false);
});
```

-----

## NoneType Error for Request A Game Form

- When submitting the form on the Request A Game page, the following error occurred: `TypeError: 'NoneType' object is not subscriptable`, which was caused by this line of code: `has_user_requested = existing_request["requested_by"]`

- If `existing_requested` was **None**, it would trigger this error. To fix the error, then, I update the code as follows:

```
if existing_request is not None:
    has_user_requested = existing_request["requested_by"]
```

- This alteration fixed the NoneType Error and allowed the form to be submitted
