from flask import (Flask, render_template, redirect, request, make_response, session, flash)
import requests
from flask_bootstrap import Bootstrap
from jinja2 import StrictUndefined
from flask_debugtoolbar import DebugToolbarExtension
from model import (LoginForm, RegisterForm, connect_to_db, db, Favorite, User)
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
def display_loginpage():
    """Show url landing page to allow users to sign in or register"""
    login_form = LoginForm()
    register_new_user_form = RegisterForm()

    return render_template('loginpage.html',
                            register_new_user_form = register_new_user_form,
                            login_form = login_form)

@login_manager.user_loader
def load_user(id):
   
    return User.query.get(int(id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Validating entered user info with the DB"""
    # import pdb; pdb.set_trace()


    login_form = LoginForm() 
    user = User.query.filter_by(username=login_form.username.data).first()
    
    if login_form.validate_on_submit():
        if user:
            if user.password == login_form.password.data:
                login_user(user)
                return redirect('/searchpage')
    else:
        flash("Sorry, the information you entered is incorrect")
        return redirect('/')


@app.route('/register', methods=['GET', 'POST'])
def register_new_user():
    """Adding a new user to the DB"""

    register_new_user_form = RegisterForm()
    user = User.query.filter_by(username=register_new_user_form.username.data).first()
    email = User.query.filter_by(email = register_new_user_form.email.data).first()
    if user or email:
        flash("Sorry, the username or email already exists in the database")
        return redirect('/')
    elif register_new_user_form.validate_on_submit():
        new_user = User(username=register_new_user_form.username.data,
                        email=register_new_user_form.email.data,
                        password=register_new_user_form.password.data)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect('/searchpage')



@app.route('/searchpage')
@login_required 
def display_search_page():
    """Displays the searchpage. This is the user's homepage"""
    # favorites = Favorite.query.filter_by(id = current_user.id).all()
    # if len(favorites) == 0:
    #     favorites = "You currently have no favorites"
    favorites = "No favorites"

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

    logout_user()
    return redirect('/')

if __name__ == '__main__':
    #setting debug to true to invoke the DebugToolBarExtension
    app.debug = True
    connect_to_db(app)
    # app.jinja_env.auto_reload = app.debug

    #Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')