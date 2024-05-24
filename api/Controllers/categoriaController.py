from flask_restful import Resource, request
from api.models import db, TCategoria 
from flask import jsonify
from flask_jwt_extended import jwt_required
import sys



## listar todas las categorías,
## crear una categoría
## modificar una categoría
## eliminar una categoría
## listar una categoría por id
## router = api.route('/categoria')
## jwt_required()
## class CategoriaController(Resource):

class CategoriaController(Resource):
    @jwt_required()
    def get(self, id=None):
        print('endpoint Categoria id', id)
        try:
            if id is not None:
                categoria = TCategoria.query.filter_by(id = id).first()

                print('resultado de la consulta de categoria', categoria)
                print('id',categoria.id)
                print(type(categoria))
                if not categoria:
                    return {'message': 'No se encontraron registros'}, 404
                # object of type response is not json serializable
                
                return jsonify(categoria), 200
            categorias = TCategoria.query.all()
            if not categorias:
                return {'message': 'No se encontraron registros'}, 404
            return jsonify([categoria.serialize() for categoria in categorias]), 200
        except:
            return str(sys.exc_info()[1]), 500
    @jwt_required()
    def post(self):
        print('endpoint Categoria post')
        try:
            data = request.get_json()
            categoria = TCategoria(nombre=data['nombre'],Eliminado=False,Activo=True)
            db.session.add(categoria)
            db.session.commit()
            return {'message': 'success'}, 200
        except:
            return str(sys.exc_info()[1]), 500
    @jwt_required()
    def put(self, id=None):
        print('endpoint Categoria put')
        try:
            data = request.get_json()
            categoria = TCategoria.query.filter_by(id=id).first()
            if not categoria:
                return {'message': 'No se encontraron registros'}, 404
            if 'nombre' in data:
                categoria.nombre = data['nombre']
            if 'Eliminado' in data:
                categoria.Eliminado = data['Eliminado']
            if 'Activo' in data:
                categoria.Activo = data['Activo']
            db.session.commit()
            return {'message': 'success'}, 200
        except:
            return str(sys.exc_info()[1]), 500
    @jwt_required()
    def delete(self, id=None):
        print('endpoint Categoria delete')
        try:
            categoria = TCategoria.query.filter_by(id=id).first()
            if not categoria:
                return {'message': 'No se encontraron registros'}, 404
            categoria.Eliminado = True
            db.session.commit()
            return {'message': 'success'}, 200
        except:
            return str(sys.exc_info()[1]), 500