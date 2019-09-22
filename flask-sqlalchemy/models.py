from database import db
from sqlalchemy import *


class Todo(db.Model):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    completed = Column(String)

    def __repr__(self):
        return "<Todo(name='%s', title='%s', completed='%s')>" % (self.id, self.title, self.completed)

    def to_obj(self):
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed
        }