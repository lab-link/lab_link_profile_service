import sys
sys.path.append('./')
from flask import Flask
from api import save_profile_wrapper
from flask_sqlalchemy import SQLAlchemy
from . import USERNAME, PASSWORD, HOST, DATABASE

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] =f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"
db = SQLAlchemy(app)

save_profile_blueprint = save_profile_wrapper(db)
app.register_blueprint(save_profile_blueprint)


# with app.app_context():
#     db.create_all()