# auth.py

import json
from flask import Blueprint, request, Response, redirect, url_for
from boto3.dynamodb.conditions import Key
from flask_login import login_user
from .models import User
from . import dynamodb

auth = Blueprint('auth', __name__)


@auth.route('/api/login', methods=['POST'])
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


@auth.route('/api/signup', methods=['POST'])
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

        return redirect(url_for('auth.login'))


@auth.route('/api/board/<int:boardId>', methods=['GET'])
def boards(boardId):
    table = dynamodb.Table('boards')
    response = table.query(
        KeyConditionExpression=Key('boardId').eq(boardId)
    )
    items = response['Items']
    return items


@auth.route('/api/logout')
def logout():
    return 'Logout'
