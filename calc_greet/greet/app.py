from flask import Flask,request

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return 'Welcome'

@app.route('/welcome/home')
def home():
    return 'Welcome Home'

@app.route('/welcome/back')
def back():
    return 'Welcome Back'