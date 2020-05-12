# Python's version used: 3.8.2 64 bit
# pip install flask
# To view the created web page
# run the script and go to localhost:5000
from flask import Flask
from flask import render_template
from flask import request
from flask import Flask, redirect, url_for, request
app = Flask(__name__)


# First page
@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['usermail']
        password = request.form['password']
        # if user and password are correct
        if user == "renzodefrancesco@gmail.com" and password == "renzo":
            # go to the dashboard
            return redirect(url_for('dashboard', name=user))
        else:
            # go to the error page
            return redirect(url_for('error'))
    else:
        user = request.args.get('name')
        return '''
<section class="loginform cf">   
    <form action = "http://localhost:5000" method = "post">
        <ul>  
            <li><label for="usermail">Email</label>  
            <input type="email" name="usermail" placeholder="yourname@email.com" required></li>  
            <li><label for="password">Password</label>  
            <input type="password" name="password" placeholder="password" required></li>  
            <li>  
            <input type="submit"></li>  
        </ul>  
    </form>
</section>
'''


# Dashboard page
@app.route('/dashboard/<name>')
def dashboard(name):
    return 'Welcome %s' % name

# Error page
@app.route('/error')
def error():
    return 'Wrong username or passoword!'


# This will make possibile to run the app
# by simply run the script
if __name__ == '__main__':
    app.run(debug=True)
