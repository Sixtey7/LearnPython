from flask import Blueprint

todo_api = Blueprint('todo_api', __name__)

@todo_api.route('/hello')
def hello():
    return "Hello World"