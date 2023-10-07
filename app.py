import sys
sys.path.append('./')
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api import get_profile_wrapper
from api import save_profile_wrapper
from api import update_profile_wrapper
from . import USERNAME, PASSWORD, HOST, DATABASE

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] =f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"
db = SQLAlchemy(app)

get_profile_blueprint = get_profile_wrapper(db)
save_profile_blueprint = save_profile_wrapper(db)
update_profile_wrapper = update_profile_wrapper(db)

app.register_blueprint(get_profile_blueprint)
app.register_blueprint(save_profile_blueprint)
app.register_blueprint(update_profile_wrapper)

# with app.app_context():
#     db.create_all()