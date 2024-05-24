from flask_restful import Resource, request
from sqlalchemy import text
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from flask import jsonify
from api.models import db, TUser
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
            if id is not None:
                registro = TUser.query.filter_by(id=id,Eliminado=False,Activo=True).first()
                if not registro:
                    return {'message': 'No se encontraron registros'}, 404
                return registro.serialize(), 200
            else:
                registro = TUser.query.filter_by(Eliminado=False,Activo=True).all()
                if not registro:
                    return {'message': 'No se encontraron registros'}, 404
                return [registro.serialize() for registro in registro], 200
           
        except:
            return str(sys.exc_info()[1]), 500
    def post(self):
        try:
            print('ingresa a post')
            data = request.get_json()
            print('data', data)
            registro = TUser(name=data['userName'],email=data['email'],password=data['password'])
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
            if 'userName' in data:
                registro.userName = data['userName']
            if 'email' in data:
                registro.email = data['email']
            if 'password' in data:
                registro.encrypt_password(data['password'])
            if 'imagen' in data:
                registro.imagen = data['imagen']
            db.session.commit()
            return {'message': 'success'}, 200
        except:
            return str(sys.exc_info()[1]), 500