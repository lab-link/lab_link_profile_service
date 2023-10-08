from lab_link_profile_service.app import db
from sqlalchemy import ForeignKey

class Institutions(db.Model):
    __tablename__ = "Institutions"
    __table_args__ = {'extend_existing': True}

    institution_id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, ForeignKey('Profiles.profile_id'))
    image_url = db.Column(db.String(250))
    institution_name = db.Column(db.String(50))
    date_started = db.Column(db.Date)
    date_ended = db.Column(db.Date, nullable=True) 
    institution_type = db.Column(db.String(50)) 
    institution_position = db.Column(db.String(50))
    is_currently_attending = db.Column(db.Boolean, default=False)
    institution_accomplishments = db.Column(db.String(1000), nullable=True) 
