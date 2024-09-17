from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from backend.app.db.models import User

jwt = JWTManager()

def hash_password(password: str) -> str:
    return generate_password_hash(password)

def verify_password(password: str, password_hash: str) -> bool:
    return check_password_hash(password_hash, password)

def create_token(user: User) -> str:
    identity = {"id": user.id, "role": user.role}
    return create_access_token(identity=identity)

# HUMAN ASSISTANCE NEEDED
# This function needs to be implemented with database interaction
def get_current_user() -> User:
    identity = get_jwt_identity()
    # TODO: Implement database query to retrieve user
    # Example: user = User.query.get(identity['id'])
    # Return the user object
    return None