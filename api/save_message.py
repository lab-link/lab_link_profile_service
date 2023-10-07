from flask import request, jsonify
from flask import Blueprint

def save_message_wrapper(db):
    from models import Messages
    save_message_blueprint = Blueprint('save_message', __name__)

    @save_message_blueprint.route("/save-message", methods=['POST'])
    def save_message():
        """
        This API stores a message into mysql.
        :param {}: JSON
        :return: string
        """

        if request.method == 'POST':
            content = request.get_json()
            message_id = content.get("message_id", None)
            message_data = content.get("message_data", None)
            user_sender_id = content.get("user_sender_id", None)
            user_reciepient_id = content.get("user_reciepient_id", None)
            timestamp = content.get("timestamp", None)
            new_message = Messages(
                message_id=message_id,
                message_data=message_data,
                user_sender_id=user_sender_id,
                user_reciepient_id=user_reciepient_id,
                timestamp=timestamp,
            )
            db.session.add(new_message)
            db.session.commit()
            return jsonify(message="Message saved successfully!"), 201
        else:
            return jsonify(message="Method not allowed"), 405
    return save_message_blueprint
