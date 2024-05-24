from flask import request, jsonify
from flask_restful import Resource
from api.models import db, TTorneo as Torneo, TInscripcion as Inscripcion, TUser as User

class torneoController(Resource):
    def get(self, id=None):
        try:
            if id is not None:
                print('id', id)
                torneo = Torneo.query.filter_by(id=id).first()
                if not torneo:
                    return {'message': 'No se encontraron registros'}, 404
                return torneo.serialize()
            else:
                print('id en el else : ', id)
                # devolver el torneo con el año más reciente
                #torneo = Torneo.query.order_by(Torneo.anio.desc()).first()
                torneo = Torneo.query.filter_by(anio=2024).first()
                print('torneo encontrado', torneo.anio)
                # unir datos de usuarios inscritos en torneo
                #torneoInscripcion = Inscripcion.query.join(Torneo).all()
                #torneoInscripcion = Inscripcion.query.join(Torneo,Torneo.id==Inscripcion.torneoId).all()
                #torneoInscripcion = db.session.query(Inscripcion,Torneo).join(Torneo,Torneo.id==Inscripcion.torneoId).all()
                inscripciones = Inscripcion.query.filter_by(torneoId=torneo.id).all()
                #inscripciones = Inscripcion.query.filter_by(torneoId=torneo.id).all()
                #.join(User,User.id==Inscripcion.luchadorId).filter(Torneo.id==torneo.id).all()
                print('torneoInscripcion', inscripciones)
                datos ={"torneo":torneo.anio,"luchadores":[]}
                for inscripcion in inscripciones:
                    datos["luchadores"].append({
                        "id":inscripcion.luchadorId,
                        "userName":inscripcion.luchador.userName,
                        "imagen":inscripcion.luchador.imagen,
                        "ki":inscripcion.ki,
                        "esferas":inscripcion.esferas,
                        "anio":torneo.anio
                    }
                       
                    )
                return jsonify(datos)
                # unir datos de torneo con datos de categoria
                #torneoCategoria = Torneo.query.join(Torneo.categoria).all()
                
        except Exception as e:
            return str(e)

    def post(self):
        try:
            data = request.get_json()
            torneo = Torneo(
                nombre=data['nombre'],
                fecha_inicio=data['fecha_inicio'],
                fecha_fin=data['fecha_fin'],
                estado=data['estado']
            )
            db.session.add(torneo)
            db.session.commit()
            return jsonify(torneo.serialize())
        except Exception as e:
            return str(e)