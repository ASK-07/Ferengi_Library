# Ferengi Game Library
> Alex Kaylor, Jaime Flores, Jake Butler, Nathan Padgett, Heath Mercer, collaborated
> to create a flask application where users can play a variety of games in their browser.


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
<!-- * [License](#license) -->

## General Information
> We originally sought to create a 2D physics engine, with a small application to demo it.
> After a semi-successful first sprint, we decided to pivot to a more approachable project.

> The project we pivoted to was a flask application where users could choose from a selection of games to play.

![Template Logo](./img/Ferengi-logos.jpeg)



## Technologies Used
> - Python
> - Javascript
> - HTML/CSS
> - Flask
> - MongoDB


## Features

> - Each view extends an HTML template that has routes for 'Open Source Games', 'About', and the homepage.

> - Homepage - The first page users are introduced to when visiting the site or launching the application.
>    - Can be accessed from any page by clicking on the 'Ferengi' image (a species from Startrek).
>    - Three grids are displayed, each with a different variety of games:
>        1. Hosted Games - A 1x2 grid of games that we integrated into our flask app
>        2. Open Source Games - A random 1x4 grid of embeddable open-source games
>        3. Other Free Games - A dynamic grid of embeddable free games
>        - Each game has an image and name that redirect to their respective pages when clicked.
>        - Both the open source games grid and the other free games grid are created using a python script that takes in a dictionary and returns an HTML string formatted for our use case.
>  

> - Open Source Games - A page where all embedded open source games that can be played on the site can be accessed.
>     - Each open source games' information is stored in a remote database. We decided to use MongoDB.
>     - The route uses a technique called pagination, which helps make our application more scalable.
>         - Currently, nine games are displayed per page.
>         - As new game information is included in the database, the open source games page(s) will automatically be updated.
>         - To navigate to different pages, links at the bottom of the page can be used to specify which page a user would like to visit.
>             - The links provide a 'First' and 'Last' page, which redirect the user to the first and last page, respectively.
>             - Between the 'First' and 'Last' links, three numbers are displayed which redirect the user to their respective page.
>     - The route is dynamic, meaning different pages are accessed using the convention: 'OpenSourceGames/page/pagenumber'.
>         - The initial route is 'OpenSourceGames/page/1'
> - About - A page that introduces each team member with their photo, email address, and a short description.

> - Each open source game is displayed using a dynamic route.
>       - Each game's route is defined as: 'OpenSourceGames/gamename'.
>       - Each game's page displays:
>           1. The game's name
>           2. An iframe element that 'embeds' the game, making it playable on the game's page
>           3. A link to the game's repository on Github
> - Each other free games' pages follow a similar layout to the open source games' pages, but without a link to the game's source code.
> - The two hosted games were modified to track each one's highest obtained scores.
>     - New high scores are automatically added to the database.
>     - The high scores are displayed on each game's respective page.



