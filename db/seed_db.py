import json

def seed_org_data(db, path_str):
    from pathlib import Path
    from models import Organizations
    path = Path(path_str)
    with open(path) as f:
        obj_arr = json.load(f)

    for obj in obj_arr:
        org = Organizations(**obj)
        db.session.add(org)
    
    db.session.commit()

