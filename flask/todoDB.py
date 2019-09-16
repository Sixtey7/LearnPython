# import sqlite3
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base


class TodoDB:
    def __init__(self):
        print('Creating the database!')

        self.engine = create_engine('sqlite:///todos.db', echo=True)

        Base = declarative_base()

        class Todo(Base):
            __tablename__ = 'todo'
            id = Column(Integer, primary_key=True)
            title = Column(String)
            completed = Column(String)

            def __repr__(self):
                return "<Todo(name='%s', title='%s', completed='%s')>" % (self.id, self.title, self.completed)

        Base.metadata.create_all(self.engine)