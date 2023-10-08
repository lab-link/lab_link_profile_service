from lab_link_profile_service.app import db
from sqlalchemy import ForeignKey

class Organizations(db.Model):
    __tablename__ = "Organizations"
    __table_args__ = {'extend_existing': True}

    organization_id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(50))
    organization_name = db.Column(db.String(70)) 
    organization_description = db.Column(db.String(1000))
    organization_milestones = db.Column(db.String(1000))
    
    positions = db.relationship('ProjectPositions', backref='organizations', lazy=True)