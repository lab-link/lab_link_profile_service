import sys
sys.path.append('./')
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from api import profile_routes_wrapper
from api import profile_portfolio_routes_wrapper
from api import institutions_routes_wrapper
from api import project_routes_wrapper
from api import project_position_routes_wrapper
from api import organization_routes_wrapper

from db import seed_profile_data
from db import seed_org_data
from db import seed_project_data

from . import USERNAME, PASSWORD, HOST, DATABASE

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"
db = SQLAlchemy(app)

profile_routes_blueprint = profile_routes_wrapper(db)
project_portfolio_blueprint = profile_portfolio_routes_wrapper(db)
institutions_blueprint = institutions_routes_wrapper(db)
project_position_blueprint = project_position_routes_wrapper(db)
project_blueprint = project_routes_wrapper(db)
organization_blueprint = organization_routes_wrapper(db)

app.register_blueprint(profile_routes_blueprint)
app.register_blueprint(project_portfolio_blueprint)
app.register_blueprint(institutions_blueprint)
app.register_blueprint(project_position_blueprint)
app.register_blueprint(project_blueprint)
app.register_blueprint(organization_blueprint)

with app.app_context():
    db.drop_all()
    db.create_all()  


@app.cli.command("seed-db")
def seed_db():
    seed_profile_data(db, '../profile_data.json')
    seed_org_data(db, '../org_data.json')
    seed_project_data(db, '../project_data.json')
    print("Database seeded!")
