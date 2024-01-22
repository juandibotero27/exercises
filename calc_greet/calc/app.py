# Put your app in here.
from flask import Flask,request

from operations import add,sub,mult,div

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Home Page</h1>'

@app.route('/add')
def my_add():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = add(a,b)
    return str(result)
    

@app.route('/sub')
def my_sub():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = sub(a,b)
    return str(result)


@app.route('/mult')
def my_mult():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = mult(a,b)
    return str(result)



@app.route('/div')
def my_div():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = div(a,b)
    return str(result)


operators = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<oper>')
def all_math(oper):
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = operators[oper](a,b)
    return str(result)