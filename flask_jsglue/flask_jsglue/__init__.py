from flask import Blueprint


bp = Blueprint("flask_jsglue", __name__, template_folder="templates")

from flask_jsglue.flask_jsglue import (
    routes,
)  # Import routes to associate them with the blueprint
