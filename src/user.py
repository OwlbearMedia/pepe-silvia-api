# user.py

import json
from flask import Blueprint, request, Response
from flask_login import login_user
from .models import User
from . import dynamodb

user = Blueprint('user', __name__)


@user.route('/api/user/login', methods=['POST'])
def login():
    requestData = request.get_json()
    email = requestData['email']
    password = requestData['password']
    user = User

    table = dynamodb.Table('users')
    response = table.get_item(
        Key={
            'email': email,
        }
    )

    if 'Item' in response:
        user = User(response['Item'])

    if password != user.password:
        res = {'error': 'Invalid login credentials'}
        return Response(
            status=401,
            mimetype='application/json',
            response=json.dumps(res)
        )

    else:
        user.authenticate()
        login_user(user, remember=True)
        return Response(status=200)


@user.route('/api/user/signup', methods=['POST'])
def signup():
    requestData = request.get_json()
    email = requestData['email']
    password = requestData['password']

    table = dynamodb.Table('users')
    response = table.get_item(
        Key={
            'email': email,
            'password': password
        }
    )
    user = response['Item']

    if user:
        res = {'error': 'User already exists'}
        return Response(
            status=400,
            mimetype='application/json',
            response=json.dumps(res)
        )

    else:
        table.put_item(
            Item={
                    'email': email,
                    'password': password,
                }
            )

        return Response(status=200)


@user.route('/api/logout')
def logout():
    return 'Logout'
