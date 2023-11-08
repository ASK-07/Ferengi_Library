# Ferengi Physics Engine
> Alex Kaylor, Jaime Flores, Jake Butler, Nathan Padgett, Heath Mercer, are collaborating
> to create and implement a simple 2d physics engine.
<!-- If you have the project hosted somewhere, include the link here. -->

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
<!-- * [License](#license) -->


## General Information
> OLD:This project is designed for users and developers
> such as ourselves interested in learning and implementing an engine such as this from the ground up. Our 
> system will be designed to be intentionally simplified to be accessible to any user and developer to
> understand comprehensively no matter their education.
>
> Update: We decided to pivot from our previous idea of creating a 2d physics engine to implementing a flask app that hosts a number of games in our website. Our website will be able to run each game and display the highest scores for the different games that we currently have available.
![Template Logo](./img/FERENGI-logos.jpeg)



## Technologies Used
- C++
- Java
- Python
- Flask
- HTML/CSS
- Javascript


## Features
List of ready features here:

- GUI - Simple and intuitive user interface, allowing the user to interact with the engine and its objects.
- Object Drawing - System will draw an object on the plane when recieving input from the user to do so.
	
	>relevant user story(s) to above features: 
    >As a user, I would like to create a window with a 2d plane and a few buttons, that when clicked draw an object.
    >As a developer I want to generate a set of objects that are either static or dynamic.
	

- Dynamics (simple movement) - System will be able to simulate movement on the objects by recieving user input.
- Gravity simulated on objects within 2D plane - System will simulate gravity on all objects in the plane.

	>relevant user story(s): 
    >As a developer, I would like to implement functions in order to change the gravity and velocities of the simulation, so that I can test different scenarios.
    >As a user, I would like a user interface within the window to generate forces upon created objects.
    >As a developer I want to generate a set of objects that are either static or dynamic.

- Plane reset - User will be able to clear the plane of all drawn objects and imposed physics.

    >relevant user story(s): 
    >As a user, I would like the ability to pause/resume the state of the engine to observe individual frames that are displayed.
    
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

- **Jake**

- **Jaime**: "As a User I would want a home page that is concise and showcases the menu for our game."
    - `Jira Task (SCRUM-72): Setting up the flask app repo from previous assignment`
        - URL: https://cs3398f23ferengi.atlassian.net/jira/software/projects/SCRUM/boards/1/backlog?epics=visible&issueParent=10064&selectedIssue=SCRUM-72
    - `Jira Task (SCRUM-75): Research the basics of HTML and CSS`
        - URL: https://cs3398f23ferengi.atlassian.net/jira/software/projects/SCRUM/boards/1/backlog?epics=visible&issueParent=10064&selectedIssue=SCRUM-75


## Next Steps
- **Alex**: "Merge game class and info to work for scoreboard, alter menu to not include game titles, import a handful of games without access to scorekeeping and add details to homepage, look into local database"

- **Nathan**:  "Implementing the backend scoreboard keeping as well as adding in the backend and frontend to a user login in page in order to give logged in users more features" 

- **Heath**:

- **Jake**

- **Jaime**: "Import another game into our flask app and work in keeping track of scores in the backend or continue to update our front-end."
