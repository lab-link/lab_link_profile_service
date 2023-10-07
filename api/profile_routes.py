from flask import request, jsonify
from flask import Blueprint

def profile_routes_wrapper(db):
    from models import Profiles
    profile_blueprint = Blueprint('profile', __name__)

    @profile_blueprint.route("/save-profile", methods=['POST'])
    def save_profile():
        """
        This API stores a profile into mysql.
        :param {}: JSON
        :return: string
        """
        if request.method == 'POST':
            content = request.get_json()
            profile_id = content.get("profile_id", None)
            firstname = content.get("firstname", None)
            lastname = content.get("lastname", None)
            title = content.get("title", None)
            employment = content.get("employment", None)
            years_of_experience = content.get("years_of_experience", None)
            skills = content.get("skills", None)
            new_profile = Profiles(
                profile_id=profile_id,
                firstname=firstname,
                lastname=lastname,
                title=title,
                employment=employment,
                years_of_experience=years_of_experience,
                skills=skills
            )
            db.session.add(new_profile)
            db.session.commit()
            return jsonify(message="Profile saved successfully!"), 201
        else:
            return jsonify(message="Method not allowed"), 405
    

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
        
    @profile_blueprint.route("/update-profile/<int:profile_id>", methods=['PUT'])
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
        
    return profile_blueprint