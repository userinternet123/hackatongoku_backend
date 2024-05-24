from . import db

class TTorneoCategoria(db.Model):
    __tablename__ = 'TTorneoCategoria'
    #__table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    torneoId = db.Column(db.Integer, db.ForeignKey('TTorneo.id'), nullable=False)
    categoriaId = db.Column(db.Integer, db.ForeignKey('TCategoria.id'), nullable=False)
    Eliminado = db.Column(db.Boolean, default=False)
    Activo = db.Column(db.Boolean, default=True)
    #torneo = db.relationship('TTorneo', backref='torneoCategoria', lazy=True)
    categoria = db.relationship('TCategoria', backref='torneoCategoriaCategoria', lazy=True)
    
    def __init__(self, torneoId, categoriaId, Eliminado=False, Activo=True):
        self.torneoId = torneoId
        self.categoriaId = categoriaId
        self.Eliminado = Eliminado
        self.Activo = Activo
    def __repr__(self):
        return '<TTorneoCategoria %r>' % self.id
    def serialize(self):
        return {
            'id': self.id,
            'torneoId': self.torneoId,
            'categoriaId': self.categoriaId,
            'Eliminado': self.Eliminado,
            'Activo': self.Activo
        }