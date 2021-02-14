"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from python_webapp_flask import app

import requests
import json

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/search')
def search():

    searchterm = request.args.get("searchterm")

    url = "https://www.googleapis.com/books/v1/volumes?q=" + searchterm + "&printType=books&maxResults=3"

    response = requests.request("GET", url)

    if(response != ""):
        return json.dumps({'status_code': 200, 'results': response.text})
    else:
        return json.dumps({'status_code': 500, 'error': 'Nothing was returned'})


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
