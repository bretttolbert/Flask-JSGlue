from flask import Blueprint

bp = Blueprint("flask_jsglue", __name__, template_folder="templates")

from flask_jsglue.main import (
    routes,  # type: ignore
)  # Import routes to associate them with the blueprint
