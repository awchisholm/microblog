from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(form.username.date, form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign in', form=form)
