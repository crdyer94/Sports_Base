from flask import (Flask, render_template, redirect, request, flash, session)
from flask_bootstrap import Bootstrap
from jinja2 import StrictUndefined
from flask_debugtoolbar import DebugToolbarExtension
from model import (User, LoginForm, RegisterForm, connect_to_db, db)
from sqlalchemy import update
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (LoginManager, login_user, login_required, logout_user, current_user)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc123'
app.jinja_env.undefined = StrictUndefined
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@app.route('/')
def index():

    return render_template('index.html') 

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
#WHY USE BOTH GET AND POST
def logIn():

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password.data):
                login_user(user, remember=form.data)
                return redirect('/searchpage')
        # return '<h1> Invalid username or password </h1>'
    #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'
    #test to make sure that I am posting data and getting data from the form

    return render_template('login.html',
                            form=form)
                            # required="")

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
        return redirect('/searchpage')

        # return '<h1> new user has been created </h1>'
        #test to make sure that a new user is being created and added to my db
    # return '<h1>' + form.username.data + ' ' + ' ' + form.password.data + ' ' + form.email.data +'</h>'
    #test to make sure taht I am posting data and getting data from the form

    return render_template('signup.html', 
                            form=form)

@app.route('/searchpage')
@login_required
def searchPage():

    return render_template('searchpage.html', name = current_user.username)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


if __name__ == '__main__':
    #setting debug to true to invoke the DebugToolBarExtension
    app.debug = True
    app.jinja_env.auto_reload = app.debug

    #Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
