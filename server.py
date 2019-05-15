from flask import (Flask, render_template, redirect, request, flash, session)
from flask_bootstrap import Bootstrap
from jinja2 import StrictUndefined
from flask_debugtoolbar import DebugToolbarExtension
from model import (User, LoginForm, RegisterForm, connect_to_db, db)
from sqlalchemy import update


app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc123'
app.jinja_env.undefined = StrictUndefined
Bootstrap(app)


@app.route('/')
def index():

    return render_template('index.html') 

@app.route('/login', methods=['GET', 'POST'])
def logIn():

    form = loginForm()

    # if form.validate_on_submit():
    #     return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'
    #test to make sure that I am posting data and getting data from the form

    return render_template('login.html',
                            form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signUp():

    form = registerForm()

    # if form.validate_on_submit():
    #     return '<h1>' + form.username.data + ' ' + ' ' + form.password.data + ' ' + form.email.data +'</h>'
    #test to make sure taht I am posting data and getting data from the form

    return render_template('signup.html', 
                            form=form)

@app.route('/dashboard')
def dashboard():

    return render_template('dashboard.html')


if __name__ == '__main__':
    #setting debug to true to invoke the DebugToolBarExtension
    app.debug = True
    app.jinja_env.auto_reload = app.debug

    #Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
