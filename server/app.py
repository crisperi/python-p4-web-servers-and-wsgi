from flask import  Flask 

app = Flask(__name__)


@app.route('/')
def index ():
    return '<h1> Welcome to my first flask page </h1>'

@app.route('/<string:username>')
def user (username):
    return f'<h1> Profile for  {username}</h1>'
