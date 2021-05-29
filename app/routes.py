from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Andrew'}
    posts = [
        {
            'author': {'username': 'Andrew'},
            'body': 'Not raining in Hampshire!'
        },
        {
            'author': {'username': 'Andrew'},
            'body': 'Doom!'
        }
    ]
    return render_template('index.html', title = 'Home', user=user, posts=posts)
