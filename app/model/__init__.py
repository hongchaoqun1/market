from flask import Blueprint

model = Blueprint("model", __name__)

from . import User