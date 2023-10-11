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
> This project is designed for users and developers
> such as ourselves interested in learning and implementing an engine such as this from the ground up. Our 
> system will be designed to be intentionally simplified to be accessible to any user and developer to
> understand comprehensively no matter their education.
>
![Template Logo](./img/FERENGI-logos.jpeg)



## Technologies Used
- C++
- Java


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

## Contributions
- **Jake**: "Designed and partially implemented classes following a state pattern design approach, implemented logic for rendering a state's frame"
	- `Jira Task (SCRUM-30): Design the interface files outlined by the class diagram`
        - URL: https://cs3398f23ferengi.atlassian.net/jira/software/projects/SCRUM/boards/1/backlog?epics=visible&issueParent=10007&selectedIssue=SCRUM-30
		- reference: https://bitbucket.org/cs3398f23ferengi/%7Bb5d91a26-2ba9-4319-8b24-98b14e7dc7c1%7D/commits/3d2ccb249cee0a98d8387adb147ce94ee524b893
	- `Jira Task (SCRUM-32): Implement classes and demonstrate state transition`
        - URL: https://cs3398f23ferengi.atlassian.net/jira/software/projects/SCRUM/boards/1/backlog?epics=visible&issueParent=10007&selectedIssue=SCRUM-32
		- reference: https://bitbucket.org/cs3398f23ferengi/%7Bb5d91a26-2ba9-4319-8b24-98b14e7dc7c1%7D/commits/95e857a6447b842b3cf6b281417deb2812f0706f
        
        