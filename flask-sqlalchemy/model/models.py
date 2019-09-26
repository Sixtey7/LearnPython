from model.database import db
from sqlalchemy import *


class Todo(db.Model):
    """Model class to store Todo objects in the database
    """
    __tablename__ = 'todo'
    id = Column(String, primary_key=True)
    title = Column(String)
    completed = Column(String)

    def __repr__(self):
        return "<Todo(name='%s', title='%s', completed='%s')>" % (self.id, self.title, self.completed)

    def to_obj(self):
        """Returns the object in JSON format
        :return String representation of the object
        """
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed
        }