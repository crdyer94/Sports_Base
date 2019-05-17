from flask import (Flask, render_template, redirect, request, flash, session)
from flask_bootstrap import Bootstrap
from jinja2 import StrictUndefined
from flask_debugtoolbar import DebugToolbarExtension
from model import (User, LoginForm, RegisterForm, connect_to_db, db)
from sqlalchemy import update
from werkzeug.security import generate_password_has, check_password_hash
from flask_login import (LoginManager, UserMixin, login_user, login_required, logout_user, current_user)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc123'
app.jinja_env.undefined = StrictUndefined
Bootstrap(app)


@app.route('/')
def index():

    return render_template('index.html') 

@app.route('/login', methods=['GET', 'POST'])
#WHY USE BOTH GET AND POST
def logIn():

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password.data):
                return redirect('/dashboard')
        return '<h1> Invalid username or password </h1>'
    #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'
    #test to make sure that I am posting data and getting data from the form

    return render_template('login.html',
                            form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signUp():

    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method= 'sha256')
        new_user = User(username=form.username.data,
                        email=form.email.data,
                        password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        # return '<h1> new user has been created </h1>'
        #test to make sure that a new user is being created and added to my db
    # return '<h1>' + form.username.data + ' ' + ' ' + form.password.data + ' ' + form.email.data +'</h>'
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
