from flask import Flask

todos = {}

app = Flask(__name__)

@app.route('/todos/healthz')
def healthz():
    return "All's Well"

@app.route('/todos', methods=['GET'])
def getAll():
    return "GET"

@app.route('/todos', methods=['POST'])
def updateObj():
    return "POST"

app.run(port=5000, debug=True)