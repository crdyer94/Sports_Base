"""Models and database functions for Sports Base."""

from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

db = SQLAlchemy()


#####################################################################
# Model definitions

class User(db.Model):
    """User of ratings website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String(64),
                        nullable=False,
                        unique=True)
    password = db.Column(db.String(64), 
                        nullable=False)
    user_name = db.Column(db.String(64),
                            nullable=False, 
                            unique=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"""<User user_id={self.user_id}, 
                    email={self.email}>"""

class LoginForm(FlaskForm):
    """Account management fields for user login"""
    username = StringField('Username',
                            validators = [InputRequired(),
                                            Length(max=64)])
    password = PasswordField('Password',
                            validators = [InputRequired(),
                                            Length(max=64)])
    remember = BooleanField('Remember Me')

class RegisterForm(FlaskForm):
    """Account management fields for user registration"""
    email = StringField('Email', 
                        validators=[InputRequired(),
                                    Email(message = 'Invalid email'),
                                    Length(max=64)])
    username = StringField('Username',
                            validators = [InputRequired(),
                                            Length(max=64)])
    password = PasswordField('Password',
                            validators = [InputRequired(),
                                            Length(max=64)])

# class Report(db.Model):
#     """Reports submitted by users."""

#     __tablename__ = "reports"

#     report_id = db.Column(db.Integer,
#                          autoincrement=True,
#                          primary_key=True)
#     user_id = db.Column(db.Integer,
#                         db.ForeignKey('users.user_id'))
#     report_description = db.Column(db.String(500), 
#                                     nullable=False)
#     report_submit_date = db.Column(db.DateTime)

#     user = db.relationship("User",
#                             backref = db.backref("reports",
#                                                 order_by=report_id))

#     def __repr__(self):
#         """Provide helpful representation when printed."""

#         return f"""<Report report_id={self.report_id},
#                     user_id={self.user_id}, 
#                     description={self.report_description}, 
#                     submitted on {report_submit_date}>"""

# class Favorite(db.Model):
#     """Athlete or team profiles favorited by a user"""

#     __tablename__ = "favorites"

#     favorite_id = db.Column(db.Integer, 
#                             autoincrement=True, 
#                             primary_key=True)
#     user_id = db.Column(db.Integer,
#                         db.ForeignKey('users.user_id'))
#     athlete_id = db.Column(db.Integer,
#                             db.ForeignKey('athletes.athlete_id'),
#                             nullable=True) 
#     team_id = db.Column(db.Integer, nullable=True) #SAME AS ABOVE
    

#     def __repr__(self):
#         """Provides helpful representation when printed."""

#         return f"<Favorite favorite_id={favorite_id}"


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
    # As a convenience, if we run this module interactively, it will
    # leave you in a state of being able to work with the database
    # directly.

    from server import app
    connect_to_db(app)
    print("Connected to DB.")
