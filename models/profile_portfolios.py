from lab_link_profile_service.app import db
from sqlalchemy import ForeignKey

class ProfilePortfolios(db.Model):
    __tablename__ = "ProfilePortfolios"
    __table_args__ = {'extend_existing': True}

    portfolio_id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, ForeignKey('Profiles.profile_id'))
    employer_name = db.Column(db.String(50)) 
    experience_data = db.Column(db.String(1000))
    
  