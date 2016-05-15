from flask import render_template, request, redirect
from application import app


@app.route('/')
def main():
    return redirect('/index')


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        params = {}
    else:
        params = {}

    return render_template('index.html', params=params)

