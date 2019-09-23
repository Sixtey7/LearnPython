from model.database import db
from model.models import Todo
from uuid import uuid4


def get_all_todos():
    return Todo.query.all()


def get_todo(todo_id):
    return Todo.query.filter_by(id=todo_id).first()


def create_todo(title, completed, todo_id=None):
    if todo_id is None:
        print('creating an id')
        todo_id = str(uuid4())

    new_todo = Todo(id=todo_id, title=title, completed=completed)

    db.session.add(new_todo)
    db.session.commit()

    return new_todo


def update_todo(todo_id, title=None, completed=None):
    todo_to_update = Todo.query.filter_by(id=todo_id).first()

    if todo_to_update is None:
        raise ValueError("Could not find Todo with id")

    if title is not None:
        todo_to_update.title = title

    if completed is not None:
        todo_to_update.completed = completed

    db.session.commit()

    return todo_to_update
