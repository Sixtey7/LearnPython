from flask import Flask
from model.database import db
from routes.todoRoutes import todo_api
from routes.todoListRoutes import todo_list_api

# Create the flask app
app = Flask(__name__)
app.register_blueprint(todo_api, url_prefix="/todos")
app.register_blueprint(todo_list_api, url_prefix="/todo-lists")

# SQLAlchemy config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///model/todos.db'
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)

db.app = app

# Create all of the tables
# Note: The below line comes back as not used, but I believe I need to import it to make sure the
# table gets created
from model.models import Todo, TodoList

db.create_all()


app.run(port=5000, debug=True)
