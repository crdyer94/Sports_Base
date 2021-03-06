"""Models and database functions for Sports Base."""

from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_login import LoginManager, UserMixin
from sqlalchemy_json import NestedMutableJson


db = SQLAlchemy()


####################################################################
# Model definitions

class User(UserMixin, db.Model):
    """User of website."""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String(64),
                        nullable=False,
                        unique=True)
    password = db.Column(db.String(64), 
                        nullable=False)
    username = db.Column(db.String(64),
                            nullable=False, 
                            unique=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"""<User id={self.id}, 
                    email={self.email}>"""


class SearchForm(FlaskForm):
    """Search fields for player search"""
    playername = StringField('Playername',
                                validators = [InputRequired()])

class LoginForm(FlaskForm):
    """Account management fields for user login"""
    username = StringField('Username:',
                            validators = [InputRequired(),
                                            Length(max=64)])
    password = PasswordField('Password:',
                            validators = [InputRequired(),
                                            Length(max=64)])

    def render_field(self, field, render_kw):
            render_kw.setdefault('required', True)
            return super().render_field(field, render_kw)

class RegisterForm(FlaskForm):
    """Account management fields for user registration"""
    email = StringField('Email:', 
                        validators=[InputRequired(),
                                    Email(message = 'Invalid email'),
                                    Length(max=64)])
    username = StringField('Username:',
                            validators = [InputRequired(),
                                            Length(max=64)])
    password = PasswordField('Password:',
                            validators = [InputRequired(),
                                            Length(max=64)])
    def render_field(self, field, render_kw):
            render_kw.setdefault('required', True)
            return super().render_field(field, render_kw)


class Favorite(db.Model):
    """Athlete profiles favorited by a user"""

    __tablename__ = "favorites"

    favorite_id = db.Column(db.Integer, 
                            autoincrement=True, 
                            primary_key=True)
    id = db.Column(db.Integer,
                        db.ForeignKey('users.id'),
                        unique=False)
    favorited_item = db.Column(db.Integer, 
                                nullable=False)
    user = db.relationship("User",
                           backref=db.backref("favorites", order_by=favorite_id))

    def __repr__(self):
        """Provides helpful representation when printed."""

        return f"<Favorite favorite_id={self.favorite_id}>"


#####################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///sportsbase'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print("Connected to DB.")
