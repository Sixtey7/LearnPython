from model.database import db
from model.models import Todo
from uuid import uuid4


def get_all_todos():
    """Returns all of the Todo objects in the database

    :returns: A list of Todo objects
    :rtype: list
    """
    return Todo.query.all()


def get_todo(todo_id):
    """Returns the Todo object specified by the provided todo_id

    :param todo_id: The id of the Todo to retrieve, nominally a UUID
    :returns A single Todo object
    :rtype Todo
    """
    return Todo.query.filter_by(id=todo_id).first()


def create_todo(title, completed, todo_id=None):
    """Creates a Todo given the provided values

    :param title: The string title of the Todo be created
    :param completed: The value of the completed attribute of the Todo
    :param todo_id: The id to assign to the todo.  If not provided, a UUID will be generated as part of creation
    :returns The created Todo object
    :rtype Todo
    """
    if todo_id is None:
        print('creating an id')
        todo_id = str(uuid4())

    new_todo = Todo(id=todo_id, title=title, completed=completed)

    db.session.add(new_todo)
    db.session.commit()

    return new_todo


def update_todo(todo_id, title=None, completed=None):
    """Updates the provided values in the specified todo

    :param todo_id The id of the Todo to be updated
    :param title If provided, the title to update the Todo with
    :param completed If provided, the completed value to set the Todo to
    :returns The updated Todo object
    :rtype Todo
    :raise ValueError if no Todo is found for the given id
    """
    todo_to_update = Todo.query.filter_by(id=todo_id).first()

    if todo_to_update is None:
        raise ValueError("Could not find Todo with id")

    if title is not None:
        todo_to_update.title = title

    if completed is not None:
        todo_to_update.completed = completed

    db.session.commit()

    return todo_to_update


def delete_todo(todo_id):
    """Deletes the Todo specified by the provided todo_id
    :param todo_id: the id of the Todo to be deleted
    :return: True if the Todo was successfully deleted
    :raise ValueError if no Todo is found for the given id
    """
    todo_to_delete = Todo.query.filter_by(id=todo_id).first()

    if todo_to_delete is None:
        raise ValueError("Could not find Todo with id")

    db.session.delete(todo_to_delete)
    db.session.commit

    return True