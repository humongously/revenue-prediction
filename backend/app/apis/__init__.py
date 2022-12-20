from .profile import api as profile_ns

from flask import Blueprint
from flask_restx import Api

blueprint = Blueprint("api", __name__)

api = Api(blueprint, title="example backend")

api.add_namespace(profile_ns, path="/profile")