from flask import jsonify, request,make_response, abort
import os
from app import app
import datetime
from app.models.user_model import UserModel
from app.validation.validate_user import validate_input

@app.route('/api/v1/auth/signup', methods=['POST'])
def create_user():
    if(not request.json or not 'name' in  request.json
                        or not 'username' in request.json
                        or not 'email' in request.json
                        or not 'password' in request.json
                        or not 'confirm_password' in request.json
                        ):
        return jsonify({'message':'All fields are required'}), 400
    data = request.get_json() or {}
    validate =validate_input(data)
    if validate != True:
        return jsonify({"message":validate_input(data)}),422

    date_created = datetime.datetime.utcnow()
    date_modified = datetime.datetime.utcnow()

    if(data['password']!=data['confirm_password']):
        return jsonify({'message':'passwords do not much'}), 422
    register_user = UserModel.register_user(data['name'], data['email'], data['username'], data['password'], date_created, date_modified)
    print(register_user)
    if register_user=='Email or username already exists':
        return jsonify({'message':register_user}), 403
    
    return jsonify({'message':register_user}), 201



