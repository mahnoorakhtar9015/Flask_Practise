from flask import Flask 

app=Flask(__name__)

@app.route('/')

def main():
    return "Welcome"


@app.route('/<name>')
    
def new_page(name):
    return f"Welcome {name}..."


@app.route('/name/<int:age>')

def my_age(age):
    return f"My age is {age}...."

@app.route('/mahnoor/<float:account>')

def my_account_money(account):
    return f"My Account has amount {account}"


if __name__=='__main__':
    app.run(debug=True)