from . import db

class TCategoriaRequerimiento(db.Model):
    __tablename__ = 'TCategoriaRequerimiento'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Eliminado = db.Column(db.Boolean, default=False)
    Activo = db.Column(db.Boolean, default=True)
    categoriaId = db.Column(db.Integer, db.ForeignKey('TCategoria.id'), nullable=False)
    requerimientoId = db.Column(db.Integer, db.ForeignKey('TRequerimiento.id'), nullable=False)
    def __init__(self, categoriaId, requerimientoId, Eliminado=False, Activo=True):
        self.categoriaId = categoriaId 
        self.requerimientoId = requerimientoId 
        self.Eliminado = Eliminado
        self.Activo = Activo
        
    def __repr__(self):
        return '<TCategoriaRequerimiento %r>' % self.id
    def serialize(self):
        return {
            'id': self.id,
            'categoriaId': self.categoriaId,
            'requerimientoId': self.requerimientoId,
            'Eliminado': self.Eliminado,
            'Activo': self.Activo
        }