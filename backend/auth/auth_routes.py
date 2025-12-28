from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth_bp", __name__)

DUMMY_USER = {"username": "admin", "password": "admin123"}

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username == DUMMY_USER["username"] and password == DUMMY_USER["password"]:
        token = create_access_token(identity=username)
        return jsonify({"token": token}), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401
