# auth.py


from flask import Blueprint, request, make_response, redirect, url_for
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

    table = dynamodb.Table('users')
    response = table.get_item(
        Key={
            'email': email,
        }
    )

    if hasattr(response, 'Item'):
        user = User(response['Item'])

    if 'user' not in locals() or password != user.password:
        response = make_response()
        return response

    login_user(user)
    return redirect(url_for('main.profile'))


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
        response = make_response()
        return response

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
