from flask import Flask, render_template, request
app = Flask(__name__)
from madlib import story
@app.route('/')
def hello():
    return render_template('base.html')

@app.route('/form')
def mad_lib():
    text = story.generate(request.args)
    return render_template('madlib.html', text=text)