# import sqlite3
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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

        Session = sessionmaker(bind=self.engine)

        self.session = Session()

        # figure out the max id
        max_id = self.session.query(func.max(Todo.id)).scalar()
        print("Max id was: %s" % max_id)
        new_todo = Todo(id=(max_id + 1), title="Hello World", completed = "false")

        self.session.add(new_todo)

        self.session.commit()

        # get the todo back out
        got_todo = self.session.query(Todo).filter_by(id=1).first()

        print(got_todo)