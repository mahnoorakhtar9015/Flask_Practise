from flask import Flask,redirect

app=Flask('__name__')

@app.route('/')

def main():
    return redirect("/helloworld")

@app.route('/helloworld')

def hello_world():
    return "Redirected from main"


if __name__=='__main__':
    app.run(debug=True)        