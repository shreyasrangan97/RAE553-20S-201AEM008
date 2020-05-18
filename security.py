#comparing the strings by importing safe_str_cmp from werkzeug.security.
from werkzeug.security import safe_str_cmp
from user import User

# authorizing username and password by comparing the strings using safe_str_cmp
def authenticate(username, password):
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user
#authorizing the user by identifying the user id.
def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)
