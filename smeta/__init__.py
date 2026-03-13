from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return '<a href="/secure">/secure</a>'


@app.route("/secure")
def secure():
    return '<a href="/">/</a><hr>hello FIXME'
