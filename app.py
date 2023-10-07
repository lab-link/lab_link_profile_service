from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet_user():
    return jsonify(message="Hello, User!")

if __name__ == "__main__":
    app.run(debug=True)