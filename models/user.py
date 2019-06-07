from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_login import LoginManager, UserMixin
from sqlalchemy_json import NestedMutableJson
from model import db

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

        return f"""<User user_id={self.id}, 
                    email={self.email}>"""
