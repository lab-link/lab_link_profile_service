from lab_link_profile_service.app import db

class Profiles(db.Model):
    __tablename__ = "Profiles"
    __table_args__ = {'extend_existing': True}

    profile_id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))  # Assuming a maximum length of 50 characters
    lastname = db.Column(db.String(50))
    title = db.Column(db.String(100))  # Titles can be a bit longer
    employment = db.Column(db.String(100))
    years_of_experience = db.Column(db.Integer)
    skills = db.Column(db.String(255))  # This could be a comma-separated list, so giving it more space


