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
        project_id = content.get("project_id")
        project_description = content.get("project_description")
        organizer_data = content.get("organizer_data")
        date_posted = content.get("date_posted")

        new_project = Projects(
            project_id=project_id,
            project_description=project_description,
            organizer_data=organizer_data,
            date_posted=date_posted
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
                'project_description': project.project_description,
                'organizer_data': project.organizer_data,
                'date_posted': now.strftime('%Y-%m-%d %H:%M:%S')
            }), 200
        else:
            return jsonify(message="Project not found"), 404
        
    @project_blueprint.route("/update-project/<int:project_id>", methods=['PUT'])
    def update_project(project_id):
        project = Projects.query.get(project_id)
        if not project:
            return jsonify(message="Project not found"), 404

        content = request.get_json()
        project.project_description = content.get("project_description", project.project_description)
        project.organizer_data = content.get("organizer_data", project.organizer_data)
        project.date_posted = content.get("date_posted", project.date_posted)

        db.session.commit()
        return jsonify(message="Project updated successfully!"), 200

    return project_blueprint
