from lab_link_profile_service.app import db
from sqlalchemy import ForeignKey

class Projects(db.Model):
    __tablename__ = 'Projects'

    project_id = db.Column(db.Integer, primary_key=True)
    project_collaborators = db.Column(db.String(200)) # also sponsored by ...
    project_description = db.Column(db.String(500)) 
    organizer_data = db.Column(db.String(500))
    date_posted = db.Column(db.String(50))

    positions = db.relationship('ProjectPositions', backref='Projects', lazy=True)
    