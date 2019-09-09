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

app.run(port=5000, debug=True)