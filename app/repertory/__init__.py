from flask import Blueprint

repertory = Blueprint("repertory", __name__)

from . import UserRepositiontory, dbconfig, DbConnection