from flask_restful import Resource, request
from sqlalchemy import text
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from flask import jsonify
from api.models import db, TPrueba, TUser
from api.Utilities.queries.query import get_query
from flask_jwt_extended import jwt_required
import sys

class userApiController(Resource):
    @jwt_required()
    def get(self, id=None):
        try:
            print('ingresa a get')
            #parsed = pd.DataFrame()
            print('id', id)
            registro = TUser.query.get(id)
            if not registro:
                return {'message': 'No se encontraron registros'}, 404
            return {'id':registro.id, 'descripcion':registro.username}, 200
        except:
            return str(sys.exc_info()[1]), 500
    def post(self):
        try:
            print('ingresa a post')
            data = request.get_json()
            print('data', data)
            registro = TUser(name=data['username'],email=data['email'],password=data['password'])
            print('agregando el registro')
            db.session.add(registro)
            db.session.commit()
            return {'message': 'success'}, 200
        except:
            return str(sys.exc_info()[1]), 500
    @jwt_required()
    def put(self, id=None):
        try:
            print('ingresa a put')
            data = request.get_json()
            registro = TUser.query.filter_by(id=id).first()
            if not registro:
                return {'message': 'No se encontraron registros'}, 404
            if 'username' in data:
                registro.username = data['username']
            if 'email' in data:
                registro.email = data['email']
            if 'password' in data:
                registro.password = data['password']
            db.session.commit()
            return {'message': 'success'}, 200
        except:
            return str(sys.exc_info()[1]), 500