from . import db

class TTorneo(db.Model):
    __tablename__ = 'TTorneo'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    anio = db.Column(db.Integer, nullable=False)
    Eliminado = db.Column(db.Boolean, default=False)
    Activo = db.Column(db.Boolean, default=True)
    
    def __init__(self, anio, Eliminado=False, Activo=True):
        self.anio = anio
        self.Eliminado = Eliminado
        self.Activo = Activo
    def __repr__(self):
        return '<TTorneo %r>' % self.id
    def serialize(self):
        return {
            'id': self.id,
            'anio': self.anio,
            'Eliminado': self.Eliminado,
            'Activo': self.Activo
        }
    