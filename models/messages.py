from lab_link_profile_service.app import db

class Messages(db.Model):
    __tablename__ = "Messages"
    __table_args__ = {'extend_existing': True}

    message_id = db.Column(db.Integer, primary_key=True)
    message_data = db.Column(db.String(1000)) 
    user_sender_id = db.Column(db.Integer)
    user_reciepient_id = db.Column(db.Integer)
    timestamp = db.Column(db.String(50)) 
  


