import json
import bcrypt
from flask import request, Response
from flask_login import login_user, login_required, logout_user
from app.models import UserModel
from app import dynamodb
from app.api import bp


def hashPassword(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


@bp.route('/user/login', methods=['POST'])
def login():
    requestData = request.get_json()
    email = requestData['email']
    password = hashPassword(requestData['password'])
    user = UserModel

    table = dynamodb.Table('users')
    response = table.get_item(
        Key={'email': email}
    )

    if 'Item' in response:
        user = UserModel(response['Item'])

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
        return Response(
            status=200,
            mimetype='application/json',
            response=json.dumps({
                'email': user.email,
                'name': user.name
            })
        )


@bp.route('/user/signup', methods=['POST'])
def signup():
    requestData = request.get_json()
    email = requestData['email']
    password = requestData['password']
    name = requestData['name']

    table = dynamodb.Table('users')
    response = table.get_item(
        Key={'email': email}
    )

    if 'Item' in response:
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
                    'password': hashPassword(password),
                    'name': name
                }
            )

        return Response(
            status=200,
            mimetype='application/json',
            response=json.dumps({
                'email': email,
                'name': name
            })
        )


@bp.route('/user/logout')
@login_required
def logout():
    logout_user()
    return Response(status=200)
