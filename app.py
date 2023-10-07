import sys
sys.path.append('./')
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api import profile_routes_wrapper
from api import profile_portfolio_routes_wrapper
from api import institutions_routes_wrapper
from api import project_routes_wrapper
from api import project_position_routes_wrapper

from . import USERNAME, PASSWORD, HOST, DATABASE

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] =f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"
db = SQLAlchemy(app)

profile_routes_blueprint = profile_routes_wrapper(db)
project_portfolio_blueprint = profile_portfolio_routes_wrapper(db)
institutions_blueprint = institutions_routes_wrapper(db)
project_position_blueprint = project_position_routes_wrapper(db)
project_blueprint = project_routes_wrapper(db)

app.register_blueprint(profile_routes_blueprint)
app.register_blueprint(project_portfolio_blueprint)
app.register_blueprint(institutions_blueprint)
app.register_blueprint(project_position_blueprint)
app.register_blueprint(project_blueprint)

# with app.app_context():
#     db.drop_all()
#     db.create_all()  