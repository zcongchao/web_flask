# coding=utf-8
from flask import Flask, request
from flask_restful import Resource, Api, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

"""
parser = reqparse.RequestParser()
parser.add_argument('admin', type=bool, help='Use super manager mode',
                    default=False)


resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'address': fields.String
}


class User(db.Model):
    __tablename__ = 'restful_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(128), nullable=True)

db.create_all()


class UserResource(Resource):
    #装饰器 marshal_with做了把模型实例的属性组合成一个字典的抽象工作
    @marshal_with(resource_fields)
    def get(self, name):
        user = User.query.filter_by(name=name).first()
        
        return user

    def put(self, name):
        address = request.form.get('address', '')
        user = User(name=name, address=address)
        db.session.add(user)
        db.session.commit()
        return {'ok': 0}, 201

    def delete(self, name):
        args = parser.parse_args()
        is_admin = args['admin']
        if not is_admin:
            return {'error': 'You do not have permissions'}
        user = User.query.filter_by(name=name).first()
        db.session.delete(user)
        db.session.commit()
        return {'ok': 0}

"""

class HelloWorld(Resource):
    def get(self):
        data = {}
        data['hello'] = "world"
        return data, 200



"""
$ http -f put http://0.0.0.0:9000/users/zou address="shenzhen"
HTTP/1.0 201 CREATED
Content-Length: 16
Content-Type: application/json
Date: Mon, 11 Mar 2019 03:23:33 GMT
Server: Werkzeug/0.14.1 Python/2.7.12

{
    "ok": 0
}


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
