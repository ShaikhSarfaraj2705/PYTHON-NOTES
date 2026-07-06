from flask import url_for

@app.route('/')
def home():
    return url_for('about')

@app.route('/about')
def about():
    return "About Page"

    