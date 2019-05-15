"""Models and database functions for Sports Base."""

from flask_sqlalchemy import SQLAlchemy

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
                        nullable=False)
    password = db.Column(db.String(64), 
                        nullable=False)
    user_name = db.Column(db.String(64),
                            nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"""<User user_id={self.user_id}, 
                    email={self.email}>"""

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

# class Team(db.Model):
#     """Team profiles"""

#     __tablename__ = "teams"

#     team_id = db.Column(db.Integer, 
#                         autoincrement=True,
#                         primary_key=True)
#     team_name = db.Column(db.String(64), 
#                             nullable=False)
#     arena_name = db.Column(db.String(64), 
#                             nullable=False)
#     arena_location = db.Column() #is this a map object, tuple??
#     owner = db.Colummn(db.String(64))
#     sport = db.Column(db.String(64), 
#                         nullable=False) 
#     league = db.Column(db.String(64), 
#                         nullable = False) 
#     team_abbreviation = db.Column(db.String(10))

#     def __repr__(self):
#         """Provides helpful representation when printed."""

#         return f"<Team team_id={team_id}, team_name = {team_name}>"


# class TeamRoster(db.Model):
#     """Association table between team records and roster records"""

#     __tablename__ = "teamRosters"

#     teamRoster_id = db.Column(db.Integer, 
#                                 autoincrement=True,
#                                 primary_key=True)
#     team_id = db.Column(db.Integer, 
#                             nullable=False) #FK NEEDED
#     roster_id = db.Column(db.Integer,
#                             nullable=False) #FK NEEDED
#      def __repr__(self):
#         """Provides helpful representation when printed."""

#         return f"<Team Roster teamRoster_id = {teamRoster_id}, team_id={team_id}>"


# class Roster(db.Model):
#     """Roster records using athlete and team data"""

#     __tablename__ = "rosters"

#     roster_id = db.Column(db.Integer,
#                             autoincrement=True,
#                             primary_key=True)
#     season_duration = db.Column(????,
#                                 nullable=False) #daterange???
#     jersey_number = db.Column(db.Integer)
#     player_position = db.Column(db.String(64))

#     def __repr__(self):
#         """Provides helpful representation when printed."""

#         return f"<Roster roster_id = {roster_id}, season  = {season_duration}>"



# IDK WHAT TO DO ABOUT BELOW:::::::::
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
