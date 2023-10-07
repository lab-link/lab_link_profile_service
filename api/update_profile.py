from flask import request, jsonify, Blueprint

def update_profile_wrapper(db):
    from models import Profiles
    update_profile_blueprint = Blueprint('update_profile', __name__)

    @update_profile_blueprint.route("/update-profile/<int:profile_id>", methods=['PUT'])
    def update_profile(profile_id):
        """
        This API updates a profile in the database.
        :param profile_id: int
        :param {}: JSON
        :return: string
        """
        if request.method == 'PUT':
            content = request.get_json()
            
            profile = Profiles.query.get(profile_id)
            if not profile:
                return jsonify(message="Profile not found"), 404
         
            profile.firstname = content.get("firstname", profile.firstname)
            profile.lastname = content.get("lastname", profile.lastname)
            profile.title = content.get("title", profile.title)
            profile.employment = content.get("employment", profile.employment)
            profile.years_of_experience = content.get("years_of_experience", profile.years_of_experience)
            profile.skills = content.get("skills", profile.skills)
            
            db.session.commit()
            return jsonify(message="Profile updated successfully!"), 200
        else:
            return jsonify(message="Method not allowed"), 405
    return update_profile_blueprint
