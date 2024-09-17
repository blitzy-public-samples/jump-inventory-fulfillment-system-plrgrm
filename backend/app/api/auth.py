from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash
from app.db.models import User
from app.core.security import validate_password

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({"error": "Invalid email or password"}), 401

    if not validate_password(password):
        return jsonify({"error": "Invalid password format"}), 400

    access_token = create_access_token(identity=user.id)
    return jsonify({"access_token": access_token}), 200

@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    # HUMAN ASSISTANCE NEEDED
    # This is a placeholder for token revocation. 
    # Implement proper token revocation mechanism based on your requirements.
    # Consider using a token blacklist or implementing stateful sessions.
    return jsonify({"message": "Successfully logged out"}), 200