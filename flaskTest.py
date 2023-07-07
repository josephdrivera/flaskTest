from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import timedelta

appFlask = Flask(__name__)

appFlask.secret_key = 'super secret key'

appFlask.permanent_session_lifetime = timedelta(minutes=5)


@appFlask.route('/')
def home():
    return render_template('index.html')


@appFlask.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    appFlask.run(debug=True)
