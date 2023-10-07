from flask import request, jsonify
from flask import Blueprint

def institutions_routes_wrapper(db):
    from models import Institutions
    institutions_blueprint = Blueprint('institutions', __name__)

    @institutions_blueprint.route("/save-institution", methods=['POST'])
    def save_institution():
        """
        This API stores an institution entry into MySQL.
        """
        content = request.get_json()
        new_institution = Institutions(
            profile_id=content.get("profile_id"),
            image_url=content.get("image_url"),
            institution_name=content.get("institution_name"),
            date_started=content.get("date_started"),
            date_ended=content.get("date_ended"),
            institution_type=content.get("institution_type"),
            is_currently_attending=content.get("is_currently_attending"),
            institution_accomplishments=content.get("institution_accomplishments")
        )
        db.session.add(new_institution)
        db.session.commit()
        return jsonify(message="Institution saved successfully!"), 201

    @institutions_blueprint.route("/get-institution/<int:institution_id>", methods=['GET'])
    def get_institution(institution_id):
        """
        This API retrieves an institution entry by its ID.
        """
        institution = Institutions.query.get(institution_id)
        if institution:
            return jsonify({
                'profile_id': institution.profile_id,
                'image_url': institution.image_url,
                'institution_name': institution.institution_name,
                'date_started': institution.date_started,
                'date_ended': institution.date_ended,
                'institution_type': institution.institution_type,
                'is_currently_attending': institution.is_currently_attending,
                'institution_accomplishments': institution.institution_accomplishments
            }), 200
        else:
            return jsonify(message="Institution not found"), 404

    @institutions_blueprint.route("/update-institution/<int:institution_id>", methods=['PUT'])
    def update_institution(institution_id):
        """
        This API updates an institution entry.
        """
        institution = Institutions.query.get(institution_id)
        if not institution:
            return jsonify(message="Institution not found"), 404

        content = request.get_json()
        institution.profile_id = content.get("profile_id", institution.profile_id)
        institution.image_url = content.get("image_url", institution.image_url)
        institution.institution_name = content.get("institution_name", institution.institution_name)
        institution.date_started = content.get("date_started", institution.date_started)
        institution.date_ended = content.get("date_ended", institution.date_ended)
        institution.institution_type = content.get("institution_type", institution.institution_type)
        institution.is_currently_attending = content.get("is_currently_attending", institution.is_currently_attending)
        institution.institution_accomplishments = content.get("institution_accomplishments", institution.institution_accomplishments)

        db.session.commit()
        return jsonify(message="Institution updated successfully!"), 200

    return institutions_blueprint
