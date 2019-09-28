from model.database import db
from model.models import TodoList
from uuid import uuid4

def get_all_todo_lists():
    """Returns all of the Todo List objects in the database

    :returns A list of Todo List objects
    :rtype: list
    """
    return TodoList.query.all()

def get_todo_list(todo_list_id):
    """Returns the Todo List object specified by the provided todo_list_id

    :param todo_list_id: The id of the Todo List to retrieve, nominally a UUID
    :returns A single TodoList object
    :rtype TodoList
    """
    return TodoList.query.filter_by(id=todo_list_id).first()

def create_todo_list(name, todo_list_id=None):
    """Creates a new Todo List given the provided values

    :param name: The name of the Todo List to be created
    :param todo_list_id: The id to assign to the todo list.  If not provided, a UUID will be generated
    :returns The created TodoList object
    :rtype TodoList
    """
    if todo_list_id is None:
        todo_list_id = str(uuid4())

    new_todo_list = TodoList(id=todo_list_id, name=name)

    db.session.add(new_todo_list)
    db.session.commit()

    return new_todo_list

