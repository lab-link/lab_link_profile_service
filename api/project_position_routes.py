from flask import request, jsonify
from flask import Blueprint

def project_position_routes_wrapper(db):
    position_blueprint = Blueprint('position', __name__)
    from models import ProjectPositions
    from datetime import datetime as dt
    now = dt.now()
    
    @position_blueprint.route("/save-project-position", methods=['POST'])
    def save_position():
        content = request.get_json()
        position_id = content.get("position_id")
        project_id = content.get("project_id")
        position_description = content.get("position_description")
        preferred_experience = content.get("preferred_experience")
        date_posted = now.strftime('%Y-%m-%d %H:%M:%S')

        new_position = ProjectPositions(
            position_id=position_id,
            project_id=project_id,
            position_description=position_description,
            preferred_experience=preferred_experience,
            date_posted=date_posted
        )
        db.session.add(new_position)
        db.session.commit()
        return jsonify(message="Project Position saved successfully!"), 201
    
    @position_blueprint.route("/get-project-position/<int:position_id>", methods=['GET'])
    def get_position(position_id):
        position = ProjectPositions.query.get(position_id)
        if position:
            return jsonify({
                'position_id': position.position_id,
                'project_id': position.project_id,
                'position_description': position.position_description,
                'preferred_experience': position.preferred_experience,
                'date_posted': position.date_posted
            }), 200
        else:
            return jsonify(message="Project Position not found"), 404
        
    @position_blueprint.route("/update-position/<int:position_id>", methods=['PUT'])
    def update_position(position_id):
        position = ProjectPositions.query.get(position_id)
        if not position:
            return jsonify(message="Project Position not found"), 404

        content = request.get_json()
        position.project_id = content.get("project_id", position.project_id)
        position.position_description = content.get("position_description", position.position_description)
        position.preferred_experience = content.get("preferred_experience", position.preferred_experience)
        position.date_posted = content.get("date_posted", position.date_posted)

        db.session.commit()
        return jsonify(message="Project Position updated successfully!"), 200

    return position_blueprint
