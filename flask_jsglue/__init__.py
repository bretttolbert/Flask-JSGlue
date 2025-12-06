from flask import Flask

from flask_jsglue.main import bp


def init(app: Flask):
    app.register_blueprint(bp)
