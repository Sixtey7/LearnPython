from flask import Blueprint, abort, jsonify, request
import model.TodoListDB as TodoListDB

todo_list_api = Blueprint('todo_list_api', __name__)


@todo_list_api.route('', methods=['GET'])
def get_all_todo_lists():
    """Returns all of the Todo Lists that exist in the database.

    :return the result as a json array
    """
    return jsonify([todo_list.to_obj() for todo_list in TodoListDB.get_all_todo_lists()]), 200


@todo_list_api.route('/<string:todo_list_id>', methods=['GET'])
def get_todo_list(todo_list_id):
    """Returns the Todo List specified by the provided  todo_list_id

    :param todo_list_id: The id of the Todo List to return
    :return 200 and the specified Todo List object, or 404 if no Todo List was found with the specified id
    """
    todo_list_object = TodoListDB.get_todo_list(todo_list_id)
    if todo_list_object is None:
        abort(404, 'No Todo List found for the given id!')

    return jsonify(todo_list_object.to_obj()), 200


@todo_list_api.route('', methods=['POST'])
def create_todo_list_obj():
    """Used to create a new Todo List

    Expects the details of the Todo List in JSON format as part of the request body
    If no id is provided, an ID will be generated as part of the Todo List creation

    :return 200 and the newly created Todo List object or 400 if no request body was found
    """
    if not request.json:
        abort(400, 'No request body provided!')

    todo_list = TodoListDB.create_todo_list(request.json['name'], request.json['id'] if 'id' in request.json else None)
    return jsonify(todo_list.to_obj()), 200


@todo_list_api.route('/<string:todo_list_id>', methods=['PUT'])
def update_todo_list_obj(todo_list_id):
    """Updates the specified Todo List with the contents of the request body (in JSON)

    :param todo_list_id: the id of the Todo List object to be updated
    :return: 200 and the updated Todo List, 400 if no request body has been provided, 404 if the specified Todo List cannot be found
    """
    if not request.json:
        abort(400, 'No request body provided')

    try:
        todo_list = TodoListDB.update_todo_list(todo_list_id, request.json['name'])
        return jsonify(todo_list.to_obj()), 200
    except ValueError:
        abort(404, 'Could not find todo list with the provided id')


@todo_list_api.route('/<string:todo_list_id>', methods=['DELETE'])
def delete_todo_list(todo_list_id):
    """Deletes the specified Todo List from the database

    :param todo_list_id: The id of the Todo List to be deleted
    :return: 200 if the Todo List was successfully deleted, 404 if the Todo List cannot be found
    """
    try:
        status = TodoListDB.delete_todo_list(todo_list_id)
        if status:
            return '', 200
        else:
            return '', 500
    except ValueError:
        abort(404, 'Could not find todo list with the provided id')