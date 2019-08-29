#Thing 1
print('---Thing 1---')

#Thing 2
print('---Thing 2---')
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='.')

@app.route('/healthz')
def healthz():
    return 'Hello'

#Thing 3
print('---Thing 3---')
@app.route('/oldHome')
def oldHome():
    return "It's alive!"

#Thing 4 and 5
print('---Thing 4 and 5---')
@app.route('/')
def home():
    thing = request.args.get('thing')
    height = request.args.get('height')
    color = request.args.get('color')
    return render_template('home.html', thing=thing, height=height, color=color)

app.run(port=5000,debug=True)