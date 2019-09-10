from flask import Flask, request, abort, jsonify
from uuid import uuid4

todos = {}

app = Flask(__name__)

@app.route('/todos/healthz')
def healthz():
    return "All's Well"

@app.route('/todos', methods=['GET'])
def getAll():
    return jsonify(todos), 200

@app.route('/todos/<string:todo_id>', methods=['GET'])
def getRoute(todo_id):
    print('Got the id %s' % todo_id)

    return jsonify(todos[todo_id])

@app.route('/todos', methods=['POST'])
def createObj():
    if not request.json:
        abort(400, 'No request body provided!')

    if 'id' in request.json:
        todoId = request.json['id']
    else:
        todoId = str(uuid4())

    todo = {
        'id': todoId,
        'title': request.json['title'],
        'complete': False
    }

    todos[todoId] = todo

    return jsonify({'todo': todo}), 201

@app.route('/todos/<string:todo_id>', methods=['PUT'])
def updateObj(todo_id):
    if not request.json:
        abort(400, 'No request body provided!')
    
    if not todos[todo_id]:
        abort(400, 'Id does not exist, use POST to create new todo')
    
    todo = {
        'id': todo_id,
        'title': request.json['title'],
        'complete': bool(request.json['complete'])
    }

    todos[todo_id] = todo

    return jsonify({'todo': todo}), 201

@app.route('/todos/<string:todo_id>/<string:complete>', methods=['PUT'])
def toggleComplete(todo_id, complete):
    if not todos[todo_id]:
        abort(400, 'Id does not exist, use POST to create new todo')

    todos[todo_id]['complete'] = bool(complete)

    return jsonify({'todo': todos[todo_id]}), 201

app.run(port=5000, debug=True)