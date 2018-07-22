from flask import Blueprint
import flask_restful as restful 

from . import authrntication, user

api = restful.Api(prefix='/api/v1')

api.add_resource(user.RegistResource, "/user/")