from flask import Flask

app=Flask(__name__)


@app.route('/')

def index():
    return "WELCOME TO INDEX PAGE"


@app.route('/hello')

def hello():
    return "WELCOME TO HELLO PAGE"

@app.route('/user/<username>')

def show_user(username):
    return f"User with username{username}"


@app.route('/post/<int:id>')
def show_post(id):
    return f"This post contain id ::: {id}"



if (__name__)==('__main__'):
    app.run(debug=True)