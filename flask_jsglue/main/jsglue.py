from markupsafe import Markup

from flask import url_for


class JSGlue:
    @staticmethod
    def include():
        js_path = url_for("serve_jsglue_js")
        return Markup('<script src="%s" type="text/javascript"></script>') % (js_path,)
