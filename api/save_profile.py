from flask import request, jsonify
from flask import Blueprint

def save_profile_wrapper(db):
    from models import Profiles
    save_profile_blueprint = Blueprint('save_profile', __name__)

    @save_profile_blueprint.route("/save-profile", methods=['POST'])
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
    return save_profile_blueprint
