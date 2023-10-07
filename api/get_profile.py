from flask import request, jsonify
from flask import Blueprint

def get_profile_wrapper(db):
    from models import Profiles
    profile_blueprint = Blueprint('get_profile', __name__)

    @profile_blueprint.route("/get-profile/<int:profile_id>", methods=['GET'])
    def get_profile(profile_id):
        """
        This API fetches a profile by ID from MySQL.
        :param profile_id: int
        :return: JSON
        """
        profile = Profiles.query.get(profile_id)
        if profile:
            return jsonify({
                'profile_id': profile.profile_id,
                'firstname': profile.firstname,
                'lastname': profile.lastname,
                'title': profile.title,
                'employment': profile.employment,
                'years_of_experience': profile.years_of_experience,
                'skills': profile.skills
            }), 200
        else:
            return jsonify(message="Profile not found"), 404
    return profile_blueprint
