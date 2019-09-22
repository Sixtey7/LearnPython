from flask import Flask, abort, jsonify
from database import db
from models import Todo

app = Flask(__name__)
# SQLAlchemy config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)

db.app = app
db.create_all()


@app.route('/todos', methods=['GET'])
def get_all():
    return jsonify([todo.to_obj() for todo in Todo.query.all()])


@app.route('/todos/<string:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo_obj = Todo.query.filter_by(id=todo_id).first()
    if todo_obj is None:
        return "Not Found", 404

    return jsonify(todo_obj.to_obj()), 200


app.run(port=5000, debug=True)
