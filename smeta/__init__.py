import logging.config

from flask import Flask
from flask.logging import default_handler

app = Flask(__name__)

try:
    app.config.from_envvar("FLASK_CONFIG", silent=False)
except (FileNotFoundError, RuntimeError) as ex:
    logging.error("Couldn't read config file: %s", ex)
app.config.from_prefixed_env()

logging.config.dictConfig({**{"version": 1}, **app.config.get("LOGGING", {})})

# Set Flasks logging handler to all loggers and enable them all
for logger in [
    logging.getLogger(name)
    for name in logging.root.manager.loggerDict  # pylint: disable=no-member
]:
    logger.handlers = [default_handler]
    logger.disabled = False


@app.route("/")
def index():
    return '<a href="/secure">/secure</a>'


@app.route("/secure")
def secure():
    return '<a href="/">/</a><hr>hello FIXME'
