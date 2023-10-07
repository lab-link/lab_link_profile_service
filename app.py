import sys
sys.path.append('./')
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api import profile_routes_wrapper
from . import USERNAME, PASSWORD, HOST, DATABASE

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] =f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"
db = SQLAlchemy(app)

profile_routes_blueprint = profile_routes_wrapper(db)

app.register_blueprint(profile_routes_blueprint)

# with app.app_context():
#     db.create_all()