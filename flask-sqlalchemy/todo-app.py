from flask import Flask, abort, jsonify, request
from model.database import db
from model.models import Todo
import model.TodoDB as TodoDB

# Create the flask app
app = Flask(__name__)

# SQLAlchemy config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///model/todos.db'
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)

db.app = app

# Create all of the tables
db.create_all()


@app.route('/todos', methods=['GET'])
def get_all():
    return jsonify([todo.to_obj() for todo in TodoDB.get_all_todos()])


@app.route('/todos/<string:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo_obj = TodoDB.get_todo(todo_id)
    if todo_obj is None:
        abort(404, 'No Todo found for given id!')

    return jsonify(todo_obj.to_obj()), 200


@app.route('/todos', methods=['POST'])
def create_obj():
    if not request.json:
        abort(400, 'No request body provided!')

    todo = TodoDB.create_todo(request.json['title'], 'false', request.json['id'] if 'id' in request.json else None)
    return jsonify(todo.to_obj()), 200


@app.route('/todos/<string:todo_id>', methods=['PUT'])
def update_obj(todo_id):
    if not request.json:
        abort(400, 'No request body provided')

    try:
        todo = TodoDB.update_todo(todo_id,
                                  request.json['title'] if 'title' in request.json else None,
                                  request.json['completed'] if 'completed' in request.json else None)
        return jsonify(todo.to_obj()), 200
    except ValueError:
        abort(404, "Could not find todo with the provided id")


@app.route('/todos/<string:todo_id>/<string: completed>', methods=['PUT'])
def set_completed(todo_id, completed):
    try:
        todo = TodoDB.update_todo(todo_id=todo_id, completed=completed)

        return jsonify(todo.to_obj()),200
    except ValueError:
        abort(404, "Could not find todo with the provided id")


app.run(port=5000, debug=True)
