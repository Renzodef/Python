# Python's version used: 3.8.2 64 bit
# pip install flask
# To view the created web page
# Go on terminal in the same directory of this file and
# If you are on Windows' terminal write: set FLASK_APP=MoneyConverter.py
# If you are on Windows' powershell write: $env:FLASK_APP = "MoneyConverter.py"
# If you are on Linux write: export FLASK_APP=MoneyConverter.py
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

@app.route("/")
def homepage():
    # HTML Code
    return '''
<!DOCTYPE html>
<html>
    <head>
        <title>Money Converter</title>       
        <!-- Angular JS library -->
        <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.4/angular.min.js">
        </script>
    </head>
    <body>
    <div ng-app ng-init="euro=1;yuan=1"> <!-- Angular JS -->
    <hr />Conversion from Euro to Yuan
    <p>Euro: <input type="text" ng-model="euro"></p>
    <p>Yuan: {{ euro*7.55 }}</p>
    <hr />Conversion from Yuan to Euro
    <p>Yuan: <input type="text" ng-model="yuan"></p>
    <p>Euro: {{ yuan*0.13 }}</p>
    <hr />
    </div>
    </body>
</html>
'''