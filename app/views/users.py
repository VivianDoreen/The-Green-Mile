from werkzeug.security import generate_password_hash, check_password_hash
from app.decorators import generate_token, token_required
from flask import jsonify, request, make_response, abort
import os
from app import app
import datetime
from app.models.user_model import UserModel
from app.validation.validate_user import validate_input
from app.validation.validate_user import validate_input_login


@app.route('/api/v1/auth/signup', methods=['POST'])
def create_user():
    if(not request.json or not 'full_name' in request.json
       or not 'username' in request.json
       or not 'email' in request.json
       or not 'password' in request.json
       or not 'confirm_password' in request.json
       ):
        return jsonify({'message': 'All fields are required'}), 400
    data = request.get_json() or {}
    validate = validate_input(data)
    if validate != True:
        return jsonify({"message": validate_input(data)}), 422

    date_created = datetime.datetime.utcnow()
    date_modified = datetime.datetime.utcnow()

    if(data['password'] != data['confirm_password']):
        return jsonify({'message': 'passwords do not much'}), 422
    register_user = UserModel.register_user(
        data['full_name'], data['email'], data['username'], data['password'], date_created, date_modified)
    if register_user == 'Email or username already exists':
        return jsonify({'message': register_user}), 403

    return jsonify({'message': register_user}), 201


@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    if (not request.json or not 'email' in request.json
            or not 'password' in request.json):
        return jsonify({"message": "wrong params"})
    data = request.get_json() or {}
    validate = validate_input_login(data)
    if validate != True:
        return jsonify({"Error": validate_input_login(data)}), 422
    user = UserModel.check_if_is_valid_user(data['email'])

    if user == "user not found":
        return jsonify({'message': 'Invalid username and password'}), 401

    return jsonify({
        'id': user[0],
        'name': user[1],
        'role': user[4],
        'email': user[2],
        'loginstatus': "Login successful",
        'x-access-token': generate_token(user[0])
    }), 200
