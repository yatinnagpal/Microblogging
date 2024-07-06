from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Mayank'}
    posts = [
        {
            'author': {'username': 'Yatin'},
            'body': 'My first day on Flask'
        },
        {
            'author': {'username': 'Nitin'},
            'body': 'My first day on Next JS'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)