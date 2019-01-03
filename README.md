# Epic7DB
Database web app for the gacha game, Epic Seven.

Currently in development in Python + Django REST + HTML/CSS/JS

__If you would like to help, please send me a message, this project will not run without the settings.py file which is currently untracked for security reasons__

# Installation

I have created a pythonenvironment for anyone who is interested in working on this project

In order to execute the app and begin contibuting, complete the following:

Step 0 - __Contact me to obtain the settings.py file. App will not run without this and the SECRET_KEY__

Step 1 - [Install Python 3.6](https://www.python.org/downloads/) or later.

Step 2  - Install pipenv.
In your command line, type,
```
pip install pipenv
```

Step 3 - Install dependencies and activate environment
Navigate to the root folder of the project and type,
``` 
pipenv shell
```
This will read the PIPFILE and install all the necessary dependencies to run the application.

Step 4 - Create your local database.
Once the environment is activated, from the root project directory, type,
```
python manage.py migrate
```
This will create a local SQLite Database file in the root directory of the app.

Step 5 - Run the Application
To run the application in development mode, type,
```
python manage.py runserver
```
By Default, it will run on 127.0.0.1:8000 and can be accessed in your web browser.


# Some of the Features I'm aiming to provide...

Character Stats

Character Skills

Character Awakening Constellations

Damage Multiplier Approximator

Artifact Information

Labrynth Maps

Catalysts and Crafting Material Locations

