from lab_link_profile_service.app import db
from sqlalchemy import ForeignKey

class ProjectPositions(db.Model):
    __tablename__ = 'ProjectPositions'

    position_id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, ForeignKey('Projects.project_id'))
    position_description = db.Column(db.String(500)) 
    preferred_experience = db.Column(db.String(500)) 
    date_posted = db.Column(db.String(50))

