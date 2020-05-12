# Python's version used: 3.8.2 64 bit
# pip install flask
# To view the created web page
# run the script and go to localhost:5000
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    animal = "dog"
    # You can pass the variable from flask to HTML in this way
    # The .html file should be in the directory "template"
    # in the same folder of the .py file
    return render_template('Render Template.html', value=animal)


# This will make possibile to run the app
# by simply run the script
if __name__ == '__main__':
    app.run(debug=True)
