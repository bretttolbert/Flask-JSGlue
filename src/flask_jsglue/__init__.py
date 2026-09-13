from typing import Optional

from flask import Flask

from flask_jsglue.main import bp


def init(app: Flask, url_prefix: Optional[str] = None):
    if url_prefix is None:
        app.register_blueprint(bp)
    else:
        app.register_blueprint(bp, url_prefix=url_prefix)
