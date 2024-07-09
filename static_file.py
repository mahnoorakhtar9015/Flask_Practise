from flask import Flask,render_template

app=Flask('__name__')

@app.route('/')


def test_static_file():
    message="Hloooooooo World"
    return render_template("test_static.html",message=message)


if __name__=='__main__':
    app.run(debug=True)