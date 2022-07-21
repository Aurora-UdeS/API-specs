import os

from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user')
def user():
    return redirect(f'{get_full_host()}:9002/apidocs')


@app.route('/expense')
def expense():
    return redirect(f'{get_full_host()}:9001/apidocs')


@app.route('/timesheet')
def timesheet():
    return redirect(f'{get_full_host()}:9000/apidocs')


@app.route('/git')
def gitactionfetcher():
    return redirect(f'{get_full_host()}:9003/apidocs', code=301)


def get_full_host():
    split_url = request.base_url.split(':')
    if len(split_url) == 3:
        method, host, _ = request.base_url.split(':')
        full_host = f'{method}:{host}'
    else:
        full_host = os.path.split(request.base_url)[0]
    return full_host


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
