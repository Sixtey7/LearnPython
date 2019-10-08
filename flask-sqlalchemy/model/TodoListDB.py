from model.database import db
from model.models import TodoList
from uuid import uuid4


def get_all_todo_lists():
    """Returns all of the Todo List objects in the database

    :return A list of Todo List objects
    :rtype: list
    """
    return TodoList.query.all()


def get_todo_list(todo_list_id):
    """Returns the Todo List object specified by the provided todo_list_id

    :param todo_list_id: The id of the Todo List to retrieve, nominally a UUID
    :return A single TodoList object
    :rtype TodoList
    """
    return TodoList.query.filter_by(id=todo_list_id).first()


def create_todo_list(name, todo_list_id=None):
    """Creates a new Todo List given the provided values

    :param name: The name of the Todo List to be created
    :param todo_list_id: The id to assign to the todo list.  If not provided, a UUID will be generated
    :return The created TodoList object
    :rtype TodoList
    """
    if todo_list_id is None:
        todo_list_id = str(uuid4())

    new_todo_list = TodoList(id=todo_list_id, name=name)

    db.session.add(new_todo_list)
    db.session.commit()

    return new_todo_list


def update_todo_list(todo_list_id, name):
    """Updates the provided Name in the specified Todo List

    :param todo_list_id: The id of the Todo List to be updated
    :param name: The name to set within the Todo List
    :return The updated Todo List object
    :rtype: TodoList
    :raise ValueError if no TodoList is found for the given id
    """
    todo_list_to_update = TodoList.query.filter_by(id=todo_list_id).first()

    if todo_list_to_update is None:
        raise ValueError("Cound not find Todo List with id")

    todo_list_to_update.name = name

    db.session.commit()

    return todo_list_to_update


def delete_todo_list(todo_list_id):
    """Deletes the Todo List specified by the provided todo_list_id

    :param todo_list_id: the id of the Todo List to be deleted
    :return True if the Todo List was successfully deleted
    :raise ValueError if no Todo List is found for the given id
    """
    todo_list_to_delete = TodoList.query.filter_by(id=todo_list_id).first()

    if todo_list_to_delete is None:
        raise ValueError("Could not found Todo List with id")

    db.session.delete(todo_list_to_delete)
    db.session.commit()

    return True
