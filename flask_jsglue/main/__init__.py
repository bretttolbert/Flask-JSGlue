from flask import Blueprint


bp = Blueprint("main", __name__, template_folder="templates")

from flask_jsglue.main import (
    routes,
)  # Import routes to associate them with the blueprint
