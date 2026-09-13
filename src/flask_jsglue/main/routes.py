import json
import re

from flask import (
    Flask,
    current_app,
    make_response,
    render_template,
)

from flask_jsglue.main import bp
from flask_jsglue.main.jsglue import JSGlue

JSGLUE_JS_PATH = "/jsglue.js"
JSGLUE_NAMESPACE = "Flask"

rule_parser = re.compile(r"<(.+?)>")
splitter = re.compile(r"<.+?>")


def get_routes(app: Flask) -> list[tuple[str, list[str], list[str]]]:
    output: list[tuple[str, list[str], list[str]]] = []
    for r in app.url_map.iter_rules():
        endpoint = r.endpoint
        if app.config["APPLICATION_ROOT"] == "/" or not app.config["APPLICATION_ROOT"]:
            rule = r.rule
        else:
            rule = f"{app.config['APPLICATION_ROOT']}{r.rule}"
        rule_args = [x.split(":")[-1] for x in rule_parser.findall(rule)]
        rule_tr = splitter.split(rule)
        output.append((endpoint, rule_tr, rule_args))
    return sorted(output, key=lambda x: len(x[1]), reverse=True)


def generate_js(app: Flask) -> str:
    rules = get_routes(app)
    # .js files are not autoescaped in flask
    return render_template("js_bridge.js", namespace=JSGLUE_NAMESPACE, rules=json.dumps(rules))


@bp.route(JSGLUE_JS_PATH)
def serve_jsglue_js():
    return make_response((generate_js(current_app), 200, {"Content-Type": "text/javascript"}))


@bp.app_context_processor
def context_processor():
    return {"JSGlue": JSGlue}
