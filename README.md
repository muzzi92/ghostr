# Name Generator

[Link to application](https://ghostr.appspot.com/)

## Local Setup
* Clone/ download repository into desired directory
* Create virtual environment
* `pip install -r requirements.txt`
* Install [Python App Engine Standard Environment](https://cloud.google.com/appengine/docs/standard/python/quickstart)
* Follow instructions to install and configure the SDK
* Run `dev_appserver.py app.yaml` to deploy the application locally

## App brief
Build an application hosted on the free version of App Engine. This application should provide a random ghost name when a user provides their own first and last name. All ghost names must be unique. The same ghost name should be consistently displayed to a returning user.
Flow:
* Overview page
  * Shows a list of user Ghost Names
  * For names which have been taken, show the email address & the name entered by the user which took the name
  * Shows a link to the Phantom name picker form: "Get a Phantom name"
  * The link to the phantom name picker form should say "Change your current Phantom name" if the user already has picked one.
* Ghost Name form
  * Should display a form for entering first and last name fields.
  * Note: Users should log-in (using Google authentication) before being able to choose/change a ghost name
* Ghost name results
  * Shows a list of 3 possible Ghost Name results for the user to select from
  * Ghost Names should be in the following format [First Name] “[Ghost Name]” [Last Name] eg: Josua “Bogle” Pedersen.
  * Allows the user to select their ghost name and return to the overview page.

### List of ghost names
https://docs.google.com/spreadsheets/d/1R-xulhVpfaXOfvx05mLK7G5WvpIRk6eJLi99UlvC8RM/edit?usp=sharing

### Technical Requirements
* Google App Engine
* Datastore
* Python v2.7
* Webapp2
* HTML/CSS/JS

## Approach
* Get familiar with tools required by spiking hello_world apps using GAE, Datastore, Webapp2
* Sift through spec and map out objects needed and functions required to communicate with each other
* Adopted a walking skeleton approach by:
    * Setting up View and Controller for the three required web pages. I added hard coded ghost names and basic forms.
    * Implementing Google User API for login.
    * Connecting Datastore and a Model for the Ghosts object. Form data pushed into the DB on selection page and the DB populates index page with it's entities.
    * Creating SpreadsheetProcessor class to pull ghost names from Google Sheets API.
    * Creating GhostDatabase wrapper class for specific and readable calls to Datastore.
    * Adding logic that handles checking if user already has ghost names and displays buttons accordingly.
    * Add logic to randomise available names.
    * Revise code and refactor.
    * Test behaviour.

## Technology Used
* Google App Engine
* Datastore
* Python v2.7
* Webapp2
* HTML/CSS
* Google Sheets API
* Google User API
* pylint
* pdbpp

## Limitations
* New Software
    * This is the first time I have used GAE, Webapp2, Datastore and the various Google APIs. As a result I spent the bulk of my time reading documentation and setting up the environment.
    * Whilst the offical documentation was clear, I ran into quite a few edgecase blockers that had not been covered in online forums. These seemed like relatively simple blockers yet took up more time than anticipated in finding solutions.
* Time
    * With only a limited amount of time to spend on this challenge, I did not manage to finesse it as much as I would have liked. See Improvements for more info.
* Front End
    * It's been a while since I've played around with the front end and had to get used to it again.

## Improvements
* More testing. It would be great to fully test this app with complete unit, interface and integration tests. I chose to put testing on the backburner due to time constraints.
* Using Key objects to access Datastore entities would have been a cleaner approach than wrapping GQL queries but took more time to get familiar with.
* Replace `GhostrEngine.setup()` function with a better approach for populating the Database prior to app launch. E.g. Running it from separate script before hand.
* Better naming. I feel like I rushed through some of the class and method naming, and hence they are not as descriptive as I would have liked.
* Further encapsulation. More logic can be extracted from the controller into modules.
* Front end. It would have been cool to spend more time styling the app and implementing some JavaScript.
