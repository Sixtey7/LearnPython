from flask import Flask, request, abort, jsonify
from uuid import uuid4
from todo import Todo

todos = {}

app = Flask(__name__)

@app.route('/todos/healthz')
def healthz():
    return "All's Well"

@app.route('/todos', methods=['GET'])
def getAll():
    #TODO: This is gnarly, I need to look into a better way to do this
    return jsonify([todos[todoId].toObj() for todoId in todos]), 200

@app.route('/todos/<string:todo_id>', methods=['GET'])
def getRoute(todo_id):
    print('Got the id %s' % todo_id)

    return jsonify(todos[todo_id].toObj())

@app.route('/todos', methods=['POST'])
def createObj():
    if not request.json:
        abort(400, 'No request body provided!')

    if 'id' in request.json:
        todoId = request.json['id']
    else:
        todoId = str(uuid4())

    todo = Todo(todoId, request.json['title'])

    todos[todoId] = todo

    return jsonify({'todo': todo.toObj()}), 201

@app.route('/todos/<string:todo_id>', methods=['PUT'])
def updateObj(todo_id):
    if not request.json:
        abort(400, 'No request body provided!')
    
    if not todos[todo_id]:
        abort(400, 'Id does not exist, use POST to create new todo')

    todo = Todo(todo_id, request.json['title'])
    todos[todo_id] = todo

    return jsonify({'todo': todo}), 201

@app.route('/todos/<string:todo_id>/<string:complete>', methods=['PUT'])
def toggleComplete(todo_id, complete):
    if not todos[todo_id]:
        abort(400, 'Id does not exist, use POST to create new todo')

    todos[todo_id]['complete'] = bool(complete)

    return jsonify({'todo': todos[todo_id].toObj()}), 201

@app.route('/todos/<string:todo_id>', methods=['DELETE'])
def deleteTodo(todo_id):
    if not todos[todo_id]:
        abort(400, 'Cannot delete an id that doesn\'t exist')
    
    del todos[todo_id]

    return '', 200

app.run(port=5000, debug=True)