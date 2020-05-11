# Python's version used: 3.8.2 64 bit
# pip install flask
# To view the created web page
# Go on terminal in the same directory of this file and
# If you are on Windows write: set FLASK_APP=Example.py
# If you are on Linux write: export FLASK_APP=Example.py
# no space between = and Example.py or it won't work
# Then: flask run
# Then go on the browser and type in the search bar:
# localhost:5000
# If you don't wanna stop and write again flask run every time you save the code again
# if you are on Windows' terminal: set FLASK_ENV=development
# if you are on Windows' powershell: $env:FLASK_ENV = "development"
# if you are on Linux: export FLASK_ENV=development
# Then: flask run
from flask import Flask

app = Flask(__name__)


# This will be displayed in the main page of the web page
# Access it by typing in the browser: localhost:5000
@app.route("/")
def homepage():
    # You can write HTML's code into the return
    return "<h1 style='color: orange'>Hello World!</h1>"


# This will be displayed in localhost:5000/contacts
@app.route("/contacts")
def contacts():
    return "Contact us!"