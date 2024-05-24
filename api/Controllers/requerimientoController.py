from flask_restful import Resource, request
from api.models import db, TRequerimiento as RequerimientoModel
from flask import jsonify
from flask_jwt_extended import jwt_required
import sys


class requerimientoController(Resource):
    @jwt_required()
    def get(self, id=None):
        try:
            if id:
                requerimiento = RequerimientoModel.query.get(id)
                if not requerimiento:
                    return {'message': 'No se encontraron registros'}, 404
                return jsonify(requerimiento.serialize()), 200
            requerimientos = RequerimientoModel.query.all()
            if not requerimientos:
                return {'message': 'No se encontraron registros'}, 404
            return jsonify([requerimiento.serialize() for requerimiento in requerimientos]), 200
        except:
            return str(sys.exc_info()[1]), 500
    @jwt_required()
    def get_by_categoria(self, id=None):
        try:
            if id:
                requerimientos = RequerimientoModel.query.filter_by(categoriaId=id).all()
                if not requerimientos:
                    return {'message': 'No se encontraron registros'}, 404
                return jsonify([requerimiento.serialize() for requerimiento in requerimientos]), 200
            
        except:
            return str(sys.exc_info()[1]), 500
    