# coding:utf-8
from flask import Blueprint
from flask_restful import Api
from .views import HelloWorld
from .views import UserResource

res = Blueprint('res', __name__)

api = Api() 
api.add_resource(HelloWorld, '/hello')
api.add_resource(UserResource, '/userres/<name>')
