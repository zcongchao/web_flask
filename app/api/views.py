# coding=utf-8
from flask import Flask, request
from flask_restful import Resource, Api, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from .. import db
from ..models import Userapi


parser = reqparse.RequestParser()
parser.add_argument('admin', type=bool, help='Use super manager mode',
                    default=False)


resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'address': fields.String
}



class UserResource(Resource):
    #装饰器 marshal_with做了把模型实例的属性组合成一个字典的抽象工作
    @marshal_with(resource_fields)
    def get(self, name):
        user = Userapi.query.filter_by(name=name).first()
        print(user)
        return user

    def put(self, name):
        address = request.form.get('address', '')
        user = Userapi(name=name, address=address)
        db.session.add(user)
        db.session.commit()
        return {'ok': 0}, 201

    def delete(self, name):
        args = parser.parse_args()
        is_admin = args['admin']
        if not is_admin:
            return {'error': 'You do not have permissions'}
        user = Userapi.query.filter_by(name=name).first()
        db.session.delete(user)
        db.session.commit()
        return {'ok': 0}



class HelloWorld(Resource):
    def get(self):
        data = {}
        data['hello'] = "world"
        print(data)
        return data, 200



"""

http -f get http://0.0.0.0:9000/users/zou
HTTP/1.0 200 OK
Content-Length: 64
Content-Type: application/json
Date: Mon, 11 Mar 2019 03:25:09 GMT
Server: Werkzeug/0.14.1 Python/2.7.12

{
    "address": "shenzhen", 
    "id": 1, 
    "name": "zou"
}
"""
