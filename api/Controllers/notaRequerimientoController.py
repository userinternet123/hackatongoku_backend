from flask_restful import Resource, request
from api.models import db, TRequerimiento as RequerimientoModel
from flask import jsonify
from flask_jwt_extended import jwt_required
import sys

class notaRequrimientoController(Resource):
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
    def put(self, id=None):
        try:
            data = request.get_json()
            requerimiento = RequerimientoModel.query.filter_by(id=id).first()
            if not requerimiento:
                return {'message': 'No se encontraron registros'}, 404
            if 'requerimientoId' in data:
                requerimiento.nombre = data['requrimientoId']
            if 'luchadorId' in data:
                requerimiento.luchardorId = data['lucharId']
            if 'torneoId' in data:
                requerimiento.categoriaId = data['torneoId']
            if 'nota' in data:
                requerimiento.nota = data['nota']
            if 'Activo' in data:
                requerimiento.Activo = data['Activo']
            if 'Eliminado' in data:
                requerimiento.Eliminado = data['Eliminado']
            db.session.commit()
            return {'message': 'success'}, 200
        except:
            return str(sys.exc_info()[1]), 500