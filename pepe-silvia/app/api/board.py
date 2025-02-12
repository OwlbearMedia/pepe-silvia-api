# main.py

import json
from flask import Response
from flask_login import login_required, current_user
from app import dynamodb
from app.api import bp


@bp.route('/')
def index():
    print('me')
    return 'ಠ_ಠ'


@bp.route('/board/<int:boardId>', methods=['GET'])
@login_required
def boards(boardId):
    table = dynamodb.Table('boards')
    response = table.get_item(
        Key={
            'boardId': boardId,
            'user': current_user.email
        }
    )

    if 'Item' in response:
        board = response['Item']
        return board
    else:
        res = {'error': 'Board not found'}
        return Response(
            status=404,
            mimetype='application/json',
            response=json.dumps(res)
        )
