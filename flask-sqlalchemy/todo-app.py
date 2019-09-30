from flask import Flask, abort, jsonify, request
from model.database import db
import model.TodoDB as TodoDB

# Create the flask app
app = Flask(__name__)

# SQLAlchemy config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///model/todos.db'
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)

db.app = app

# Create all of the tables
# Note: The below line comes back as not used, but I believe I need to import it to make sure the
# table gets created
from model.models import Todo
db.create_all()


@app.route('/todos', methods=['GET'])
def get_all():
    """Returns all of the Todos that exist in the database.

    :return the result as a json array"""
    return jsonify([todo.to_obj() for todo in TodoDB.get_all_todos()]), 200


@app.route('/todos/<string:todo_id>', methods=['GET'])
def get_todo(todo_id):
    """Returns the Todo specified by the specified todo_id

    :param todo_id: The id of the Todo to return
    :return: 200 and the specified Todo object, or 404 if no Todo was found with the specified id
    """
    todo_obj = TodoDB.get_todo(todo_id)
    if todo_obj is None:
        abort(404, 'No Todo found for given id!')

    return jsonify(todo_obj.to_obj()), 200


@app.route('/todos', methods=['POST'])
def create_obj():
    """Used to create a new Todo.

    Expects the details of the Todo in JSON format as part of the request body
    If no id is provided, an ID will be generated as part of the Todo creation

    :return: 200 and the newly created Todo object or 400 if no request body was found
    """
    if not request.json:
        abort(400, 'No request body provided!')

    todo = TodoDB.create_todo(request.json['title'], 'false', request.json['id'] if 'id' in request.json else None)
    return jsonify(todo.to_obj()), 200


@app.route('/todos/<string:todo_id>', methods=['PUT'])
def update_obj(todo_id):
    """Updates the specified Todo with the contents of the request body (in JSON)

    Expects either (or both) of "title" and "completed" to be provided in the request body

    :param todo_id: the id of the Todo object to be updated
    :return: 200 and the updated Todo, 400 if no request body has been provided, 404 if the specified Todo cannot be found
    """
    if not request.json:
        abort(400, 'No request body provided')

    try:
        todo = TodoDB.update_todo(todo_id,
                                  request.json['title'] if 'title' in request.json else None,
                                  request.json['completed'] if 'completed' in request.json else None)
        return jsonify(todo.to_obj()), 200
    except ValueError:
        abort(404, "Could not find todo with the provided id")


@app.route('/todos/<string:todo_id>/<string:completed>', methods=['PUT'])
def set_completed(todo_id, completed):
    """Sets the completed state of the specified Todo to the specified completed value

    :param todo_id: The id of the Todo to be updated
    :param completed: The value to set the completed attribute to
    :return 200 and the updated Todo, or 404 if the Todo cannot be found
    """
    try:
        todo = TodoDB.update_todo(todo_id=todo_id, completed=completed)

        return jsonify(todo.to_obj()),200
    except ValueError:
        abort(404, "Could not find todo with the provided id")


@app.route('/todos/<string:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Deletes the specified Todo from the database

    :param todo_id: The id of the Todo to be deleted
    :return: 200 if the Todo was successfully deleted, 404 if the Todo cannot be found
    """
    try :
        status = TodoDB.delete_todo(todo_id)
        if status:
            return '', 200
        else:
            return '', 500
    except ValueError:
        abort(404, "Could not find todo with the provided id")


app.run(port=5000, debug=True)
