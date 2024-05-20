import os
import sys
import pandas as pd
from flask_restful import Resource, request
from sqlalchemy import text
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from flask import jsonify
from api.models import db, TPrueba
from api.Utilities.queries.query import get_query
from flask_jwt_extended import jwt_required

#dbPrueba="mssql+pyodbc://usrUnisis25:usrUnisis25@unisis25/prueba?driver=SQL+Server+Native+Client+11.0"

print(os.getenv('dbPrueba'))
#engine = create_engine(os.getenv('dbPrueba'))
#engine = db.create_engine(dbPrueba)
#Session = sessionmaker(bind=engine)
#session = Session()

class PruebaApiController(Resource):
    @jwt_required()
    def get(self, id=None):
        try:
            ##return {'message': 'success'}, 200
            print('ingresa a get')
            parsed = pd.DataFrame()
            print('id', id)
            #query = get_query(fecha_inicial, fecha_final)
            #print('query', query)
            #parsed = pd.read_sql_query(query, db.engine)
            #parsed = pd.read_sql(query, db.engine)
            registro = TPrueba.query.get(id)
            #response = parsed.to_json(orient='records')
            if not registro:
                return {'message': 'No se encontraron registros'}, 404
            
            #response = registro.to_dict(orient='records')
            #return jsonify(parsed),200
            return {'id':registro.id, 'descripcion':registro.descripcion}, 200
        except:
            #logging_ilu.error(str(sys.exc_info()[1]))
            return str(sys.exc_info()[1]), 500
    def put(self, id=None):
        try:
            print('ingresa a post')
            
            data = request.get_json()
            registro = TPrueba.query.filter_by(id=id).first()
            if not registro:
                return {'message': 'No se encontraron registros'}, 404
            if 'descripcion' in data:
                registro.descripcion = data['descripcion']
            
            db.session.commit()
            
            #print('data', data)
            #parsed = pd.DataFrame(data)
            #parsed.to_sql('prueba', con=db.engine, if_exists='append', index=False)
            return {'message': 'success'}, 200
        except:
            #logging_ilu.error(str(sys.exc_info()[1]))
            return str(sys.exc_info()[1]), 500
    def post(self):
        try:
            print('ingresa a post')
            data = request.get_json()
            print('data', data)
            #parsed = pd.DataFrame(data)
            #parsed.to_sql('prueba', con=db.engine, if_exists='append', index=False)
            registro = TPrueba(descripcion=data['descripcion'])
            db.session.add(registro)
            db.session.commit()
            return {'message': 'registro creado','id':registro.id}, 201
        except:
            #logging_ilu.error(str(sys.exc_info()[1]))
            return str(sys.exc_info()[1]), 500