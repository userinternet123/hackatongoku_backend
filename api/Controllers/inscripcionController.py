from api.models import db, TInscripcion as Inscripcion, TNotaRequerimiento as NotaRequerimiento, TUser as User
from flask import request, jsonify
from flask_restful import Resource

class inscripcionController(Resource):
    def get(self, id=None):
        try:
            if id is not None:
                inscripcion = Inscripcion.query.filter_by(luchadorId=id).first()
                if not inscripcion:
                    return {'message': 'No se encontraron registros'}, 404
                
                detalleInscripcion = {
                    "id": inscripcion.luchador.id,
                    "userName": inscripcion.luchador.userName,
                    "imagen": inscripcion.luchador.imagen,
                    "torneoId": inscripcion.torneo.id,
                    "torneoAnio": inscripcion.torneo.anio,
                    "luchadorId": inscripcion.luchador.id,
                    "ki": str(inscripcion.ki),
                    "esferas": inscripcion.esferas,
                    "categoria": {}
                }
                
                for torneo_categoria in inscripcion.torneo.torneoCategoria:
                    categoria_info = {
                        "detalle": torneo_categoria.categoria.nombre,
                        "requerimientos": []
                    }
                    for categoria_requerimiento in torneo_categoria.categoria.categoriaRequerimiento:
                        requerimiento_info = {
                            "id": categoria_requerimiento.id,
                            "descripcion": categoria_requerimiento.requerimiento.descripcion,
                            "notas": []
                        }
                        
                        notas = NotaRequerimiento.query.filter_by(
                            requerimientoId=categoria_requerimiento.requerimientoId,
                            luchadorId=inscripcion.luchadorId,
                            torneoId=inscripcion.torneoId
                        ).all()
                        
                        for nota in notas:
                            requerimiento_info["notas"].append({
                                "id": nota.id,
                                "nota": str(nota.nota)
                            })
                        
                        categoria_info["requerimientos"].append(requerimiento_info)
                        
                    detalleInscripcion["categoria"][torneo_categoria.categoria.nombre] = categoria_info
                
                
                
                return detalleInscripcion 
            else:
                print('id en el else : ', id)
                inscripciones = Inscripcion.query.all()
                datos ={"inscripciones":[]}
                for inscripcion in inscripciones:
                    datos["inscripciones"].append({
                        "id":inscripcion.id,
                        "torneoId":inscripcion.torneoId,
                        "luchadorId":inscripcion.luchadorId,
                        "ki":inscripcion.ki,
                        "esferas":inscripcion.esferas
                    }
                       
                    )
                return jsonify(datos)
        except Exception as e:
            return str(e)

    def post(self):
        try:
            data = request.get_json()
            inscripcion = Inscripcion(
                torneoId=data['torneoId'],
                luchadorId=data['luchadorId'],
                ki=data['ki'],
                esferas=data['esferas']
            )
            db.session.add(inscripcion)
            db.session.commit()
            return jsonify(inscripcion.serialize())
        except Exception as e:
            return str(e)