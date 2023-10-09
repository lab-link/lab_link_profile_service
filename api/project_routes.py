from flask import request, jsonify
from flask import Blueprint

def project_routes_wrapper(db):
    project_blueprint = Blueprint('project', __name__)
    from models import Projects
    from datetime import datetime as dt
    now = dt.now()

    @project_blueprint.route("/save-project", methods=['POST'])
    def save_project():
        content = request.get_json()
        new_project = Projects(
            project_id=content.get("project_id"),
            project_name=content.get("project_name"),
            project_url_on_catalog=content.get("project_url_on_catalog"),
            project_url_external=content.get("project_url_external"),
            project_description=content.get("project_description"),
            project_keywords=content.get("project_keywords"),
            project_owners=content.get("project_owners"),
            project_collaborators=content.get("project_collaborators"),
            project_fields_of_science=content.get("project_fields_of_science"),
            project_is_active=content.get("project_is_active", False),
            project_geographical_scope=content.get("project_geographical_scope"),
            project_targeted_groups=content.get("project_targeted_groups"),
            projects_tasks=content.get("projects_tasks"),
            project_started_date=content.get("project_started_date"),
            project_email=content.get("project_email"),
            date_posted=content.get("date_posted"),
            organization_id=content.get("organization_id")
        )
        db.session.add(new_project)
        db.session.commit()
        return jsonify(message="Project saved successfully!"), 201
    
    @project_blueprint.route("/get-project/<int:project_id>", methods=['GET'])
    def get_project(project_id):
        project = Projects.query.get(project_id)
        if project:
            return jsonify({
                'project_id': project.project_id,
                'project_name': project.project_name,
                'project_url_on_catalog': project.project_url_on_catalog,
                'project_url_external': project.project_url_external,
                'project_description': project.project_description,
                'project_keywords': project.project_keywords,
                'project_owners': project.project_owners,
                'project_collaborators': project.project_collaborators,
                'project_fields_of_science': project.project_fields_of_science,
                'project_is_active': project.project_is_active,
                'project_geographical_scope': project.project_geographical_scope,
                'project_targeted_groups': project.project_targeted_groups,
                'projects_tasks': project.projects_tasks,
                'project_started_date': project.project_started_date,
                'project_email': project.project_email,
                'date_posted': project.date_posted,
                'organization_id': project.organization_id
            }), 200
        else:
            return jsonify(message="Project not found"), 404
        
    @project_blueprint.route("/get-all-projects", methods=['GET'])
    def get_all_projects():
        projects = Projects.query.all()
        project_list = []

        for project in projects:
            project_data = {
                'project_id': project.project_id,
                'project_name': project.project_name,
                'project_url_on_catalog': project.project_url_on_catalog,
                'project_url_external': project.project_url_external,
                'project_description': project.project_description,
                'project_keywords': project.project_keywords,
                'project_owners': project.project_owners,
                'project_collaborators': project.project_collaborators,
                'project_fields_of_science': project.project_fields_of_science,
                'project_is_active': project.project_is_active,
                'project_geographical_scope': project.project_geographical_scope,
                'project_targeted_groups': project.project_targeted_groups,
                'projects_tasks': project.projects_tasks,
                'project_started_date': project.project_started_date,
                'project_email': project.project_email,
                'date_posted': project.date_posted,
                'organization_id': project.organization_id
            }
            project_list.append(project_data)

        return jsonify(projects=project_list), 200
        
    @project_blueprint.route("/update-project/<int:project_id>", methods=['PUT'])
    def update_project(project_id):
        project = Projects.query.get(project_id)
        if not project:
            return jsonify(message="Project not found"), 404

        content = request.get_json()
        # Updating all the fields based on the JSON received
        for key, value in content.items():
            if hasattr(project, key):  # This checks if the attribute exists in the Project model
                setattr(project, key, value)
        
        db.session.commit()
        return jsonify(message="Project updated successfully!"), 200

    return project_blueprint
