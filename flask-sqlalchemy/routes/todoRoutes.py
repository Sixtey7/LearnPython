from flask import Blueprint, abort, jsonify, request
import model.TodoDB as TodoDB

todo_api = Blueprint('todo_api', __name__)


@todo_api.route('', methods=['GET'])
def get_all_todos():
    """Returns all of the Todos that exist in the database.

    :return the result as a json array
    """
    return jsonify([todo.to_obj() for todo in TodoDB.get_all_todos()]), 200


@todo_api.route('/<string:todo_id>', methods=['GET'])
def get_todo(todo_id):
    """Returns the Todo specified by the specified todo_id

    :param todo_id: The id of the Todo to return
    :return: 200 and the specified Todo object, or 404 if no Todo was found with the specified id
    """
    todo_obj = TodoDB.get_todo(todo_id)
    if todo_obj is None:
        abort(404, 'No Todo found for given id!')

    return jsonify(todo_obj.to_obj()), 200


@todo_api.route('/list/<string:todo_list_id>', methods=['GET'])
def get_todos_for_list(todo_list_id):
    """Returns the Todos that are within the list specified by todo_list_id

    :param todo_list_id: The id of the Todo List to find Todos for
    :return: 200 and a list of Todo objects
    """

    return jsonify([todo.to_obj() for todo in TodoDB.get_todos_for_list(todo_list_id)]), 200


@todo_api.route('', methods=['POST'])
def create_todo_obj():
    """Used to create a new Todo.

    Expects the details of the Todo in JSON format as part of the request body
    If no id is provided, an ID will be generated as part of the Todo creation

    :return: 200 and the newly created Todo object or 400 if no request body was found
    """
    if not request.json:
        abort(400, 'No request body provided!')

    todo = TodoDB.create_todo(request.json['title'], 'false',
                              request.json['id'] if 'id' in request.json else None,
                              request.json['list_id'] if 'list_id' in request.json else None)
    return jsonify(todo.to_obj()), 200


@todo_api.route('/<string:todo_id>', methods=['PUT'])
def update_todo_obj(todo_id):
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


@todo_api.route('/<string:todo_id>/<string:completed>', methods=['PUT'])
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


@todo_api.route('/<string:todo_id>', methods=['DELETE'])
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
