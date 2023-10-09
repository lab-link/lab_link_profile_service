import json
from pathlib import Path

def seed_profile_data(db, path_str):
    from models import Profiles
    path = Path(path_str)
    with open(path) as f:
        profile_data = json.load(f)

    for _dict in profile_data:
        profile = Profiles(**_dict)
        db.session.add(profile)
    db.session.commit()
    
def seed_org_data(db, path_str):
    from models import Organizations
    path = Path(path_str)
    with open(path) as f:
        obj_arr = json.load(f)

    for i, obj in enumerate(obj_arr):
        profile_id = (i % 7) + 1
        obj['profile_id'] = profile_id 
        org = Organizations(**obj)
        db.session.add(org)
    db.session.commit()

def seed_project_data(db, path_str):
    from models import Projects
    from models import Organizations
    path = Path(path_str)
    with open(path) as f:
        proj_arr = json.load(f)

    for proj_dict in proj_arr:
        project_owners = proj_dict.get('project_owners', None)
        if project_owners:
            for project_owner in project_owners.split(','):
                if len(project_owner) > 1:
                    organization = Organizations.query.filter_by(organization_name=project_owner).first()
                    if organization:
                        proj_dict['organization_id'] = organization.organization_id
                        proj_dict['project_is_active'] = proj_dict['project_is_active'] == 'active'
                        project = Projects(**proj_dict)
                        db.session.add(project)
    db.session.commit()

