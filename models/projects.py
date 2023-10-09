from lab_link_profile_service.app import db
from sqlalchemy import ForeignKey

class Projects(db.Model):
    __tablename__ = 'Projects'
    
    project_id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(200))
    project_url_on_catalog = db.Column(db.String(150))
    project_url_external = db.Column(db.String(250))
    project_description = db.Column(db.String(7000)) 
    project_keywords = db.Column(db.String(1000))
    project_owners = db.Column(db.String(200))
    project_collaborators = db.Column(db.String(200)) # also sponsored by ...
    project_fields_of_science = db.Column(db.String(1000))
    project_is_active = db.Column(db.Boolean, default=False)
    project_geographical_scope = db.Column(db.String(1000))
    project_targeted_groups = db.Column(db.String(1000))
    projects_tasks = db.Column(db.String(250))
    project_started_date = db.Column(db.String(50))
    project_email = db.Column(db.String(50))
    date_posted = db.Column(db.String(50))

    organization_id = db.Column(db.Integer, ForeignKey('Organizations.organization_id'))
    
    positions = db.relationship('ProjectPositions', backref='projects', lazy=True)
    


    