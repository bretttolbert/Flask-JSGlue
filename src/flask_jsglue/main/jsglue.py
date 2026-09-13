from flask import url_for
from markupsafe import Markup


class JSGlue:
    @staticmethod
    def include():
        js_path = url_for("flask_jsglue.serve_jsglue_js")
        return Markup('<script src="%s" type="text/javascript"></script>' % (js_path,))
