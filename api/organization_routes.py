from flask import request, jsonify
from flask import Blueprint

def organization_routes_wrapper(db):
    from models import Organizations
    organization_blueprint = Blueprint('organization', __name__)

    @organization_blueprint.route("/get-all-organizations", methods=['GET'])
    def get_all_organizations():
        """
        This API retrieves all organization entries.
        """
        organizations = Organizations.query.all()
        
        if organizations:
            return jsonify([
                {
                    'organization_id': organization.organization_id,
                    'image_url': organization.image_url,
                    'organization_name': organization.organization_name,
                    'organization_description': organization.organization_description,
                    'organization_milestones': organization.organization_milestones,
                    'profile_id': organization.profile_id
                } for organization in organizations
            ]), 200
        else:
            return jsonify(message="No organizations found"), 404

    return organization_blueprint
