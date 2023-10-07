from flask import request, jsonify
from flask import Blueprint

def get_message_wrapper(db):
    from models import Messages
    message_blueprint = Blueprint('get_messages', __name__)

    @message_blueprint.route("/get-message/<int:message_id>", methods=['GET'])
    def get_message(message_id):
        """
        This API fetches a message by ID from MySQL.
        :param message_id: int
        :return: JSON
        """
        message = Messages.query.get(message_id)
        if message:
            return jsonify({
                'message_id': message.message_id,
                'message_data': message.message_data,
                'user_sender_id': message.user_sender_id,
                'user_reciepient_id': message.user_reciepient_id,
                'timestamp': message.timestamp,
            }), 200
        else:
            return jsonify(message="Message not found"), 404
    return message_blueprint
