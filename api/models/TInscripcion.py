from . import db

class TInscripcion(db.Model):
    __tablename__ = 't_inscripcion'
    __table_args__ = {'extend_existing': True}
    '''Este argumento se usa para indicar que si la tabla ya existe en la base de datos, SQLAlchemy debe extender la definición existente de la tabla con cualquier cambio adicional especificado en el modelo. Esto es útil durante el desarrollo cuando estás modificando el esquema de una tabla sin querer eliminar y recrear la tabla completa. Permite que los cambios en el modelo (como agregar nuevas columnas) se apliquen a la tabla existente sin perder los datos existentes.'''

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    luchadorId = db.Column(db.Integer, db.ForeignKey('TUser.id'), nullable=False)
    torneoId = db.Column(db.Integer, db.ForeignKey('TTorneo.id'), nullable=False)
    ki = db.Column(db.double, nullable=False)
    esferas = db.Column(db.Integer, nullable=False)
    Eliminado = db.Column(db.Boolean, default=False)
    Activo = db.Column(db.Boolean, default=True)
    def __init__(self, luchadorId, torneoId, ki, esferas, Eliminado=False, Activo=True):
        self.luchadorId = luchadorId 
        self.torneoId = torneoId 
        self.ki = ki
        self.esferas = esferas
        self.Eliminado = Eliminado
        self.Activo = Activo
   
    def __repr__(self):
        '''Este método está configurado para devolver una cadena que representa una instancia de TInscripcion, incluyendo su id. Por ejemplo, si el id de una instancia es 123, la salida de __repr__ sería <TInscripcion 123>'''
        return '<TInscripcion %r>' % self.id
    def serialize(self):
        return {
            'id': self.id,
            'luchadorId': self.luchadorId,
            'torneoId': self.torneoId,
            'ki': self.ki,
            'esferas': self.esferas,
            'Eliminado': self.Eliminado,
            'Activo': self.Activo
            
        }