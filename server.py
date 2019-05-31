from flask import (Flask, render_template, redirect, request, make_response)
import requests
from flask_bootstrap import Bootstrap
from jinja2 import StrictUndefined
from flask_debugtoolbar import DebugToolbarExtension
from model import (User, LoginForm, RegisterForm, connect_to_db, db, Favorite)
from sqlalchemy import update
from flask_login import (LoginManager, login_user, login_required,
                        logout_user, current_user)
from msf import get_search_results, get_athlete_info, get_stats
# from nflarrest import get_arrests
from twitter import get_player_tweets


app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc123'
app.jinja_env.undefined = StrictUndefined
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'logIn'

@app.route('/')
def index():
    """Show login page"""

    return render_template('index.html') 

@login_manager.user_loader
def load_user(id):

    return User.query.get(int(id))


@app.route('/login', methods=['GET', 'POST'])
def logIn():
    """ Validating entered user info with the DB"""

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.password == form.password.data:
                login_user(user, remember=form.data)
                return redirect('/searchpage')
 
    #tested to make sure that I am posting data and getting data from the form

    return render_template('login.html',
                            form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signUp():
    """Adding a new user to the DB"""

    form = RegisterForm()

    if form.validate_on_submit():
        new_user = User(username=form.username.data,
                        email=form.email.data,
                        password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return render_template('searchpage.html')

        #tested to make sure that a new user is being created and added to my db
    #tested to make sure taht I am posting data and getting data from the form

    return render_template('signup.html', 
                            form=form)

@app.route('/searchpage')
@login_required
def searchPage():
    """Displays the searchpage. This is the user's homepage"""


    return render_template('searchpage.html')

@app.route('/searchresults', methods=['POST'])
def searchResults():

    playername = request.form['playername']

    playername = get_search_results(playername)


    # return player_name: Test to verify request.form

    return render_template('searchresults.html',
                            playername=playername)

@app.route('/athletes/<athlete_id>')
def displayAthleteInfo(athlete_id):
    """Athlete profile page"""

    athlete_info = get_athlete_info(athlete_id)
    results = get_stats(athlete_id)
    # arrests = get_arrests(athlete_id)
    tweets = get_player_tweets(athlete_id)

    return render_template('athlete.html', 
                            athlete_info = athlete_info, 
                            results=results, 
                            tweets = tweets)


@app.route("/setfavorites/<athlete_id>", methods=['POST'])
def setFavorite(athlete_id):
    """Associates the user to their favorited athlete"""

    favorite  = Favorite(id=current_user.id, favorited_item=athlete_id)
    db.session.add(favorite)

    db.session.commit()

    return redirect(f"/searchpage")

@app.route('/logout')
@login_required
def logout():
    """Logs out the user"""
    
    logout_user()
    return render_template('index.html')


if __name__ == '__main__':
    #setting debug to true to invoke the DebugToolBarExtension
    app.debug = True
    connect_to_db(app)
    # app.jinja_env.auto_reload = app.debug

    #Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
