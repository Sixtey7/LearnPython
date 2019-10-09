from model.database import db
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Todo(db.Model):
    """Model class to store Todo objects in the database
    """
    __tablename__ = 'todo'
    id = Column(String, primary_key=True)
    title = Column(String)
    completed = Column(String)
    list_id = Column(String, ForeignKey('todo-list.id'))

    def __repr__(self):
        return "<Todo(id='%s', title='%s', completed='%s', list_id='%s')>" % (self.id, self.title, self.completed, self.list_id)

    def to_obj(self):
        """Returns the object in JSON format
        :return String representation of the object
        """
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed,
            'list_id': self.list_id
        }


class TodoList(db.Model):
    """Model class to store Todo List objects in the database
    """
    __tablename__ = 'todo-list'
    id = Column(String, primary_key=True)
    name = Column(String)
    todos = relationship("Todo")

    def __repr__(self):
        return "<TodoList(id='%s', name='%s')>" % (self.id, self.name)

    def to_obj(self):
        """Returns the object in JSON format
        :return String represenation of the object
        """

        return {
            'id': self.id,
            'name': self.name
        }
