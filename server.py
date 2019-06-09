from flask import (Flask, render_template, redirect, request, make_response, session)
import requests
from flask_bootstrap import Bootstrap
from jinja2 import StrictUndefined
from flask_debugtoolbar import DebugToolbarExtension
from model import (LoginForm, RegisterForm, connect_to_db, db, Favorite, User)
# from models.user import User
from sqlalchemy import update
from flask_login import (LoginManager, login_user, login_required,
                        logout_user, current_user)
from mysportsfeed import get_search_results, get_athlete_info, get_stats
from nflarrest import get_arrests
from twitter import get_player_tweets


app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc123'
app.jinja_env.undefined = StrictUndefined
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.route('/')
def homepage():
    """Show homepage to allow users to sign in or register"""
    login_form = LoginForm()
    register_new_user_form = RegisterForm()

    return render_template('homepage.html',
                            register_new_user_form = register_new_user_form,
                            login_form = login_form)

@login_manager.user_loader
def load_user(id):

    return User.query.get(int(id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Validating entered user info with the DB"""

    login_form = LoginForm() 

    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user:
            if user.password == login_form.password.data:
                # login_user(user, remember=form.data)
                return redirect('/searchpage')
 
    #tested to make sure that I am posting data and getting data from the form

    return redirect('/')


@app.route('/register', methods=['GET', 'POST'])
def register_new_user():
    """Adding a new user to the DB"""

    register_new_user_form = RegisterForm()

    if register_new_user_form.validate_on_submit():
        new_user = User(username=register_new_user_form.username.data,
                        email=register_new_user_form.email.data,
                        password=register_new_user_form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return render_template('searchpage.html')

        #tested to make sure that a new user is being created and added to my db
    #tested to make sure taht I am posting data and getting data from the form

    return redirect('/')


@app.route('/searchpage')
@login_required
def display_search_page():
    """Displays the searchpage. This is the user's homepage"""
    favorites = Favorite.query.filter_by(id = current_user.id).all()

    return render_template('searchpage.html',
                            favorites=favorites)

@app.route('/searchresults', methods=['POST'])
def display_search_results():

    playername = request.form['playername']

    playername = get_search_results(playername)

    return render_template('searchresults.html',
                            playername=playername)

@app.route('/athletes/<athlete_id>')
def display_athlete_info(athlete_id):
    """Athlete profile page"""

    athlete_info = get_athlete_info(athlete_id)
    career_stats = get_stats(athlete_id)
    arrests = get_arrests(athlete_id)
    tweets = get_player_tweets(athlete_id)
    session["athlete_id"] = athlete_id

    return render_template('athlete.html', 
                            athlete_info = athlete_info,
                            athlete_id = athlete_id, 
                            career_stats=career_stats,
                            arrests=arrests, 
                            tweets = tweets)


@app.route("/addfavorite", methods=['POST'])
def set_favorite():
    """Associates the user to their favorited athlete"""
    favorite  = Favorite(id=current_user.id, favorited_item=session["athlete_id"])
    db.session.add(favorite) 

    db.session.commit()

    return redirect("/searchpage")

@app.route("/removefavorite", methods=['POST'])
def remove_favorite():
    """Removes the association of the user to the favorited athlete"""
    #search for athlete id in the favorites table
    #remove the row from the table

    favorite = Favorite.query.filter_by(id = current_user.id,
                            favorited_item = session["athlete_id"]).first()

    db.session.delete(favorite)
    db.session.commit()

    
    return redirect("/searchpage")

@app.route('/logout')
@login_required
def logout():
    """Logs out the user"""
    del session[athlete_id]
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
