import re

pattern = re.compile(r"^[a-zA-Z]{2,50}(?:[\s_-]{1}[a-zA-Z]+)*$")
pattern_email = re.compile(r'[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]{2,4}')
pattern_password = re.compile(r'^[a-zA-Z0-9]{5,100}.*[\s.]*$')
def user_validate_name(data):
    full_name = data['full_name']
    if len(full_name) < 1:
        return "fullname is required"
    if not isinstance(full_name, str):
        return "fullname input must be a string"
    if not pattern.match(full_name):
        return "fullname must begin with a letter"
    return True

def user_validate_username(data):
    username = data['username']
    if len(username) < 1:
        return "username is required"
    if not isinstance(username, str):
        return "username input must be a string"
    if not pattern.match(username):
        return "username must begin with a letter"
    return True

def user_validate_email(data):
    email = data['email']
    if len(email) < 1:
        return "email is required"
    if not isinstance(email, str):
        return "email input must be a string"
    if not pattern_email.match(email):
        return "Wrong email format"
    return True

def validate_password(data):
    password = data['password']
    if password == "":
        return "password is required"
    if not isinstance(password, str):
        return "email input must be a string"
    if not pattern_password.match(password):
        return "password must be atleast 5 characters"
    return True

def validate_confirm_password(data):
    confirm_password = data['confirm_password']
    if confirm_password == "":
        return "confirm_password is required"
    if not isinstance(confirm_password, str):
        return "email input must be a string"
    if not pattern_password.match(confirm_password):
        return "confirm_password must be atleast 5 characters"
    return True

def validate_input(data):
    validate_all = {
        "full_name": user_validate_name(data),
        "username": user_validate_username(data),
        "email": user_validate_email(data),
        "password": validate_password(data),
        "confirm_password": validate_confirm_password(data),
    }
    if validate_all['full_name'] != True:
        return validate_all['full_name']
    if validate_all['username'] != True:
        return validate_all['username']
    if validate_all['email'] != True:
        return validate_all['email']
    if validate_all['password'] != True:
        return validate_all['password']
    if validate_all['confirm_password'] != True:
        return validate_all['confirm_password']

    return True
