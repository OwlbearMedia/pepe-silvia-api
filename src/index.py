from flask import Flask
import boto3
from boto3.dynamodb.conditions import Key, Attr
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

app.wsgi_app = ProxyFix(
  app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

@app.route('/')
def hello_world():
  return "Hello, World!"

@app.route('/api/board/<int:boardId>', methods=['GET'])
def boards(boardId):
  table = dynamodb.Table('boards')
  response = table.query(
    KeyConditionExpression=Key('boardId').eq(boardId)
  )
  items = response['Items']
  return items

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5328)
   