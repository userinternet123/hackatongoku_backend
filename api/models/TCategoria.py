from . import db

class TCategoria(db.Model):
    __tablename__ = 'TCategoria'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    Eliminado = db.Column(db.Boolean, nullable=False, default=False)
    Activo = db.Column(db.Boolean, nullable=False, default=True)
    def __init__(self, nombre, Eliminado=False, Activo=True):
        self.nombre = nombre
        self.Eliminado = Eliminado
        self.Activo = Activo
    def __repr__(self):
        return '<TCategoria %r>' % self.id
    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'Eliminado': self.Eliminado,
            'Activo': self.Activo
        }
