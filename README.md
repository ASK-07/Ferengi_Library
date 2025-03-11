# Ferengi Game Library
> Alex Kaylor, Jaime Flores, Jake Butler, Nathan Padgett, Heath Mercer, collaborated
> to create a flask application where users can play a variety of games in their browser.

> We deployed our flask app, and it can be accessed [here](www.ferengigamelibrary.com).
> We only own the domain for a limited time, so if it can't be accessed, it likely needs to be renewed.

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

    
# Sprint 1
## Contributions
- **Jake**: "Designed and partially implemented classes following a state pattern design approach, implemented logic for rendering a state's frame"
	- `Jira Task (SCRUM-30): Design the interface files outlined by the class diagram`
        - URL: https://cs3398f23ferengi.atlassian.net/jira/software/projects/SCRUM/boards/1/backlog?epics=visible&issueParent=10007&selectedIssue=SCRUM-30
		- reference: https://bitbucket.org/cs3398f23ferengi/%7Bb5d91a26-2ba9-4319-8b24-98b14e7dc7c1%7D/commits/3d2ccb249cee0a98d8387adb147ce94ee524b893
	- `Jira Task (SCRUM-32): Implement classes and demonstrate state transition`
        - URL: https://cs3398f23ferengi.atlassian.net/jira/software/projects/SCRUM/boards/1/backlog?epics=visible&issueParent=10007&selectedIssue=SCRUM-32
		- reference: https://bitbucket.org/cs3398f23ferengi/%7Bb5d91a26-2ba9-4319-8b24-98b14e7dc7c1%7D/commits/95e857a6447b842b3cf6b281417deb2812f0706f
        

## Next Steps
- **Jake**: "Implementing full logic to switch states, drawing to windows depending on the engine state simulating a completed product"


## Sprint 2
>UPDATE: We decided as a group to pivot from our previous sprint 1 project to creating a flask app that will host and run games.

## Contributions
- **Alex**: "Designed a form for a webpage that contains a game element, and a scoreboard that will display high scores of previous players."
    - 'Jira Task (SCRUM-79): Collaborate for the successful import, display, and functionality of a game element'
        - URL: https://cs3398f23ferengi.atlassian.net/browse/SCRUM-79?atlOrigin=eyJpIjoiMmVlNjM3ODEyOTM0NDc3NDgwMzg3MzdjZTMwYjc5N2IiLCJwIjoiaiJ9
        - Reference: https://bitbucket.org/cs3398f23ferengi/%7Bb5d91a26-2ba9-4319-8b24-98b14e7dc7c1%7D/pull-requests/43
    - 'Jira Task (SCRUM-76): Final formatting for scoreboard in main.css'
        - URL: https://cs3398f23ferengi.atlassian.net/browse/SCRUM-76?atlOrigin=eyJpIjoiZDNiNWM1YmQzNjM5NDA5NjliOTYzYjNhNDFhZDRkNGQiLCJwIjoiaiJ9
        - Reference: https://bitbucket.org/cs3398f23ferengi/%7Bb5d91a26-2ba9-4319-8b24-98b14e7dc7c1%7D/pull-requests/44
    - 'Jira Task (SCRUM-77): Implement routes for game webpage'
        - URL: https://cs3398f23ferengi.atlassian.net/browse/SCRUM-77?atlOrigin=eyJpIjoiNDUwY2I3MjY3Yjk4NGJmNGE4NTllOTRjZGJkOWJjMDgiLCJwIjoiaiJ9
        - Reference: https://bitbucket.org/cs3398f23ferengi/%7Bb5d91a26-2ba9-4319-8b24-98b14e7dc7c1%7D/pull-requests/28
    - 'Jira Task (SCRUM-74): Design layout of game webpage'
        - https://cs3398f23ferengi.atlassian.net/browse/SCRUM-74?atlOrigin=eyJpIjoiZTliMWUyMWE1MDIxNDZkYzgzZGNkN2UzZWMwOTMzNGMiLCJwIjoiaiJ9
        - Reference: https://bitbucket.org/cs3398f23ferengi/%7Bb5d91a26-2ba9-4319-8b24-98b14e7dc7c1%7D/pull-requests/27
    - 'Jira Task (SCRUM-78): Develop scoreboard functionality for high score displays (pending access to database)
        - URL: https://cs3398f23ferengi.atlassian.net/browse/SCRUM-78?atlOrigin=eyJpIjoiMmVjYzM3ZTc5ODI3NGMyNDk0M2UyNjY2ZGY2Y2RjYzAiLCJwIjoiaiJ9
        - Reference: https://bitbucket.org/cs3398f23ferengi/%7Bb5d91a26-2ba9-4319-8b24-98b14e7dc7c1%7D/pull-requests/33
        
- **Nathan**: "Deployed a pinball game to our flask app, made the game fit the overall theme of our website, and started work on how to implement a backend scoreboard"
    - `Jira Task (SCRUM-54): Research about SFML deployment to a flask app`
        - URL: https://cs3398f23ferengi.atlassian.net/browse/SCRUM-54?atlOrigin=eyJpIjoiNzhjNjNmYWM1YWJiNDFhOWI0NzkxYWYwMjFjZDUxOTEiLCJwIjoiaiJ9
        - Reference: https://bitbucket.org/cs3398f23ferengi/%7Bb5d91a26-2ba9-4319-8b24-98b14e7dc7c1%7D/pull-requests/29
    - `Jira Task (SCRUM-55): Deploy the pinball game into flask`
        - URL: https://cs3398f23ferengi.atlassian.net/browse/SCRUM-55?atlOrigin=eyJpIjoiODY4YzAxODZhNGZlNGUzMWFkZDk0N2RlY2QwNWQ0ZGIiLCJwIjoiaiJ9
        - Reference: https://bitbucket.org/cs3398f23ferengi/%7Bb5d91a26-2ba9-4319-8b24-98b14e7dc7c1%7D/pull-requests/34
    - `Jira Task (SCRUM-56): Implement the game template so the pinball game displays nicer`
        - URL: https://cs3398f23ferengi.atlassian.net/browse/SCRUM-56?atlOrigin=eyJpIjoiMzJiNzBlNWZkYzYxNGY4NjkzZmYyZWYyYzRmY2E2Y2QiLCJwIjoiaiJ9
        - Reference: https://bitbucket.org/cs3398f23ferengi/%7Bb5d91a26-2ba9-4319-8b24-98b14e7dc7c1%7D/pull-requests/38
    - `Jira Task (SCRUM-57): Parse backend score keeping`
        - URL: https://cs3398f23ferengi.atlassian.net/browse/SCRUM-57?atlOrigin=eyJpIjoiNjlmZDQ1OTIwMTdjNGRjNGJlY2Q4MjM0ODI0ZjIxZjMiLCJwIjoiaiJ9
        - Reference: https://bitbucket.org/cs3398f23ferengi/%7Bb5d91a26-2ba9-4319-8b24-98b14e7dc7c1%7D/pull-requests/39
        - Not merged since this task was to see how the pinball game we have was storing the highscores and would break the layout of the site. 
    - `Repo for the pinball game used`
        - URL: https://github.com/corehtml5canvas/code/blob/master/ch09/pinball/pinball.html
        

- **Heath**:

- **Jake**: "Created an initial interface for users to navigate the site."
    - Jira Task (SCRUM-60): Create a grid to display available games on the home page
        - URL: https://cs3398f23ferengi.atlassian.net/browse/SCRUM-60
        - Reference: https://bitbucket.org/cs3398f23ferengi/%7Bb5d91a26-2ba9-4319-8b24-98b14e7dc7c1%7D/pull-requests/40
    - Jira Task (SCRUM-62): Add titles, descriptions of games to their respective grid positions
        - URL: https://cs3398f23ferengi.atlassian.net/browse/SCRUM-62
        - Reference: https://bitbucket.org/cs3398f23ferengi/%7Bb5d91a26-2ba9-4319-8b24-98b14e7dc7c1%7D/pull-requests/41
    - Jira Task (SCRUM-63): Add images for games to their respective grid positions
        - URL: https://cs3398f23ferengi.atlassian.net/browse/SCRUM-63 
        - Reference: https://bitbucket.org/cs3398f23ferengi/%7Bb5d91a26-2ba9-4319-8b24-98b14e7dc7c1%7D/pull-requests/45
    - Jira Task (SCRUM-64): Add redirect to title, image on click
        - URL: https://cs3398f23ferengi.atlassian.net/browse/SCRUM-64
        - Reference: https://bitbucket.org/cs3398f23ferengi/%7Bb5d91a26-2ba9-4319-8b24-98b14e7dc7c1%7D/pull-requests/46

- **Jaime**: "As a User I would want a home page that is concise and showcases the menu for our game."
    - `Jira Task (SCRUM-72): Setting up the flask app repo from previous assignment`
        - URL: https://cs3398f23ferengi.atlassian.net/jira/software/projects/SCRUM/boards/1/backlog?epics=visible&issueParent=10064&selectedIssue=SCRUM-72
    - `Jira Task (SCRUM-75): Research the basics of HTML and CSS`
        - URL: https://cs3398f23ferengi.atlassian.net/jira/software/projects/SCRUM/boards/1/backlog?epics=visible&issueParent=10064&selectedIssue=SCRUM-75


## Next Steps
- **Alex**: "Merge game class and info to work for scoreboard, alter menu to not include game titles, import a handful of games without access to scorekeeping and add details to homepage, look into local database"

- **Nathan**:  "Implementing the backend scoreboard keeping as well as adding in the backend and frontend to a user login in page in order to give logged in users more features" 

- **Heath**:

- **Jake**: "Integrating a remote database with our flask app, and exploring ideas with open source games"

- **Jaime**: "Import another game into our flask app and work in keeping track of scores in the backend or continue to update our front-end."

## Sprint 3
>UPDATE: We have added multiple new games to our library, fixed some styling, added a database that records highscores and the games, and added a new way to dynamically add "Open Source Games"

## Contributions
- **Alex**: 
    - `Jira Task (SCRUM-85): Research: implementations of unique HTML styling`
        - URL: https://cs3398f23ferengi.atlassian.net/browse/SCRUM-85?atlOrigin=eyJpIjoiNWYxZWEzNGMyMTBkNGMwNmJlYzdmN2NjYjFjN2I3MGIiLCJwIjoiaiJ9
    - `Jira Task (SCRUM-88): Update menu UI`
        - URL: https://cs3398f23ferengi.atlassian.net/browse/SCRUM-88?atlOrigin=eyJpIjoiMmRiYTIzOTk3NzRlNGU0ODgwZTA4YWNkNWU4Njg1YzUiLCJwIjoiaiJ9
    - `Jira Task (SCRUM-91): Add about us/about our library`
        - URL: https://cs3398f23ferengi.atlassian.net/browse/SCRUM-91?atlOrigin=eyJpIjoiZGQ1OTY2ODYwZjA2NGQ3ZGE5YzY4NDQ5NzNjM2QyNjYiLCJwIjoiaiJ9
    - `Jira Task (SCRUM-92): Update main.css, style choices for containers, overall background and texts/title`
        - URL: https://cs3398f23ferengi.atlassian.net/browse/SCRUM-92?atlOrigin=eyJpIjoiMmMzZGFhZDNhNjBkNDQ3MTgwODc4YzQxZjliM2ZjZGYiLCJwIjoiaiJ9
    - `Jira Task (SCRUM-94): Collaborate to get scorekeeping operating correctly for local games via database`
        - URL: https://cs3398f23ferengi.atlassian.net/browse/SCRUM-94?atlOrigin=eyJpIjoiOWM1YzU4MmIyYmQ5NDMxZmE1NjMzNDJiNWQ0ZmE2NWUiLCJwIjoiaiJ9
    - `Jira Task (SCRUM-111): Block: Reversion of code part three the threequel (added task to address merge complications)`
        - URL: https://cs3398f23ferengi.atlassian.net/browse/SCRUM-111?atlOrigin=eyJpIjoiNTFhNWY5MDYwNGU0NDU0NWI3MmEyNmYwM2I3ZmUxM2IiLCJwIjoiaiJ9
        
- **Nathan**: "Deployed a new game to replace chess from last sprint to resolve issues, added code inorder to collect scores from both pinball and 2048, added code to write those scores to the database"
    - `Jira Task (SCRUM-87): Deploy new game to replace chess`
        - URL: https://cs3398f23ferengi.atlassian.net/jira/software/projects/SCRUM/issues/SCRUM-87?jql=project%20%3D%20%22SCRUM%22%20and%20assignee%20%3D%20currentUser%28%29%20ORDER%20BY%20created%20DESC
    - `Jira Task (SCRUM-89): Bug fix current image problems`
        - URL: https://cs3398f23ferengi.atlassian.net/jira/software/projects/SCRUM/issues/SCRUM-89?jql=project%20%3D%20%22SCRUM%22%20and%20assignee%20%3D%20currentUser%28%29%20ORDER%20BY%20created%20DESC
    - `Jira Task (SCRUM-90): Fix styling issues`
        - URL: https://cs3398f23ferengi.atlassian.net/jira/software/projects/SCRUM/issues/SCRUM-90?jql=project%20%3D%20%22SCRUM%22%20and%20assignee%20%3D%20currentUser%28%29%20ORDER%20BY%20created%20DESC
    - `Jira Task (SCRUM-83): Implement backend scorekeeping for pinball`
        - URL: https://cs3398f23ferengi.atlassian.net/jira/software/projects/SCRUM/issues/SCRUM-83?jql=project%20%3D%20%22SCRUM%22%20and%20assignee%20%3D%20currentUser%28%29%20ORDER%20BY%20created%20DESC
    - `Jira Task (SCRUM-86): Connect backend scorekeeping for pinball to database`
        - URL: https://cs3398f23ferengi.atlassian.net/jira/software/projects/SCRUM/issues/SCRUM-86?jql=project%20%3D%20%22SCRUM%22%20and%20assignee%20%3D%20currentUser%28%29%20ORDER%20BY%20created%20DESC
    - `Jira Task (SCRUM-112): Connected backend scorekeeping for 2048 to the database(DO NOT MERGE  THIS DUE TO CONFLICTS)`
        - URL: https://cs3398f23ferengi.atlassian.net/jira/software/projects/SCRUM/issues/SCRUM-112?jql=project%20%3D%20%22SCRUM%22%20and%20assignee%20%3D%20currentUser%28%29%20ORDER%20BY%20created%20DESC
        - The conflicts were later fixed and the code was added into the dev3 branch
- **Heath**:

- **Jake**: "Created and integrated a remote database with our flask app, wrote a RESTful API to interact with the databsae, designed dynamic route for collection of open source games, designed route for individual open source games"
    - Jira Task (SCRUM-97): Create and integrate a remote database with the flask app
        - URL: https://cs3398f23ferengi.atlassian.net/jira/software/projects/SCRUM/boards/1?issueParent=10094&selectedIssue=SCRUM-97
        - Reference: https://bitbucket.org/cs3398f23ferengi/%7Bb5d91a26-2ba9-4319-8b24-98b14e7dc7c1%7D/pull-requests/48
    - Jira Task (SCRUM-98): Create a development endpoint for inserting embedded games to the DB
        - URL: https://cs3398f23ferengi.atlassian.net/jira/software/projects/SCRUM/boards/1?issueParent=10094&selectedIssue=SCRUM-98
        - Reference: https://bitbucket.org/cs3398f23ferengi/%7Bb5d91a26-2ba9-4319-8b24-98b14e7dc7c1%7D/pull-requests/64
    - Jira Task (SCRUM-100): Modify homepage to include hosted/opensource/freegames
        - URL: https://cs3398f23ferengi.atlassian.net/jira/software/projects/SCRUM/boards/1?issueParent=10094&selectedIssue=SCRUM-100
        - Reference: https://bitbucket.org/cs3398f23ferengi/%7Bb5d91a26-2ba9-4319-8b24-98b14e7dc7c1%7D/pull-requests/71
    - Jira Task (SCRUM-106): Write code to access and play games stored in the OpenSourceGames collection
        - URL: https://cs3398f23ferengi.atlassian.net/jira/software/projects/SCRUM/boards/1?issueParent=10094&selectedIssue=SCRUM-106
        - Reference: https://bitbucket.org/cs3398f23ferengi/%7Bb5d91a26-2ba9-4319-8b24-98b14e7dc7c1%7D/pull-requests/68
    - Jira Task (SCRUM-108): Research connection conventions depending on driver selection
        - URL: https://cs3398f23ferengi.atlassian.net/jira/software/projects/SCRUM/boards/1?issueParent=10094&selectedIssue=SCRUM-108
        - Reference: https://bitbucket.org/cs3398f23ferengi/%7Bb5d91a26-2ba9-4319-8b24-98b14e7dc7c1%7D/pull-requests/51

- **Jaime**: 


