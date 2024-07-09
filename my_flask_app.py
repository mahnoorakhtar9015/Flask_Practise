from flask import Flask,redirect,url_for,request
app= Flask(__name__)

@app.route('/success/<name>')


def success(name):
    return f"Hello {name}"


@app.route ('/login', methods=['POST','GET'] )

def login():
    if request.method == 'POST':
        user = request.form['nm']
    else:
        user = request.args.get('nm')
        
    if user:
        return redirect(url_for('success', name=user))
    else:
        return "User name not provided!"



if __name__== '__main__':
    app.run(debug=True)