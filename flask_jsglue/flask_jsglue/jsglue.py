from markupsafe import Markup

from flask import Flask, url_for

from flask_jsglue.main import bp


class JSGlue(object):
    def __init__(self, app: Flask):
        self.app = app
        app.register_blueprint(bp)

    @staticmethod
    def include():
        js_path = url_for("serve_jsglue_js")
        return Markup('<script src="%s" type="text/javascript"></script>') % (js_path,)
