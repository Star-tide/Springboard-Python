# Put your app in here.
from operations import *
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def main():
    return '''
    <html>
        <body>
            <h1>Welcome to the Calc website</h1>
        </body>
    </html>
    '''

operators = {
    'add' : add,
    'sub' : sub,
    'mult': mult,
    'div': div
}

@app.route('/<math>')
def router(math):
    a = request.args['a']
    b = request.args['b']
    return operators[math](a,b)