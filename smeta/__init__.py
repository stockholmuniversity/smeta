import logging

from flask import Flask

app = Flask(__name__)

try:
    app.config.from_envvar("FLASK_CONFIG", silent=False)
except (FileNotFoundError, RuntimeError) as ex:
    logging.error("Couldn't read config file: %s", ex)
app.config.from_prefixed_env()


@app.route("/")
def index():
    return '<a href="/secure">/secure</a>'


@app.route("/secure")
def secure():
    return '<a href="/">/</a><hr>hello FIXME'
