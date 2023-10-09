from flask import request, jsonify
from flask import Blueprint

def organization_routes_wrapper(db):
    from models import Organizations, Projects  # Import the Projects model
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

    @organization_blueprint.route("/get-organization-by-project-id/<int:project_id>", methods=['GET'])
    def get_organization_by_project_id(project_id):
        """
        This API retrieves the organization associated with a specific project by project_id.
        """
        project = Projects.query.get(project_id)

        if project:
            organization = project.organizations
            if organization:
                return jsonify({
                    'organization_id': organization.organization_id,
                    'image_url': organization.image_url,
                    'organization_name': organization.organization_name,
                    'organization_description': organization.organization_description,
                    'organization_milestones': organization.organization_milestones,
                    'profile_id': organization.profile_id
                }), 200
            else:
                return jsonify(message="Organization not found for this project"), 404
        else:
            return jsonify(message="Project not found"), 404

    return organization_blueprint
