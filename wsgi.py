import logging

from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user')
def user():
    return redirect('http://127.0.0.1:9002/apidocs')


@app.route('/expense')
def expense():
    return redirect('http://127.0.0.1:9001/apidocs')


@app.route('/timesheet')
def timesheet():
    return redirect('http://127.0.0.1:9000/apidocs')


@app.route('/git')
def gitactionfetcher():
    return redirect('http://127.0.0.1:9003/apidocs', code=301)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
