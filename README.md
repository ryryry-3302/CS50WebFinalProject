# CS50WebFinalProject
Presenting my Capstone project for CS50 Web 2022 StudyBuddy

# Introduction 
Studybuddy is a web application that aim to help youth with their education through various web-based apps

# Quick Start guide

Firstly, install the modules in the requirements.txt file.

Secondly, before running the test server visit http://cors-anywhere.herokuapp.com/ and enable demo testing to enable use of http://cors-anywhere.herokuapp.com/'s proxy to access zenquotes api.

Finally, you should be able to run the server by after cd studybuddy > python3 manage.py runserver.

After creating an account and signing in the use of the website should be self explanatory.


# Features

## User Registration
Makes use of Django's user model and login verification to easilyadd in user registration and login.

## Daily motivational quotes

Using Javascript to fetch dynamically and update daily quotes source from Zenquote's free api, through my own cors-anywhere server hosted on heroku.

# Application

## Task manager
Using django models to seamlessly create task in the sql database. Users can edit, finish and review previous completed tasks.

# Distinctiveness and Complexity

Firstly, my project is a web application aimed at being usedby individual users to help manage their schedules nad properly task their using a simple aesthetic interface as well as being kept motivated by quotes that are sourced through an api from another website. My project does not base either of these features from last years Capstone project Pizza, or the other 2 projects in this years syllabus.

Secondly, my project makes use of models to rerpresent the tasks that users creates in the task manager making it easily to access and debug using the django admin tool as well as add changes to these task if need be to add more fields. Additionally using the django model utility allows me to use model forms to use the module to automatically generate aesthetic forms using crispy forms additionally without manually typing the html.

Lastly, through my use of bootstrap 5 containers and grid I have made my project mobile responsive making the website easy to use no matter screen sizes.

# Some Challenges Faced

As I am fetching my quote from an external API not made by myself, I encountered issues using fetch as chrome blocked the request due to the CORS policy, to workaround this I've used cors-anywhere another opensource project used to serve as a proxy to avoid this problem. I believe if this server is deployed on another web hosting service this would no be a problem. Alternatively, I could also search a django model containing a csv of a bank of quotes and add it to my project file as well.


# Features to add in the future
## Flip cards
## Pomodoro timer
## Exam Scheduler
