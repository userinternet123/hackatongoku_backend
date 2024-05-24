from . import db

class TNotaRequerimiento(db.Model):
    __tablename__ = 'TNotaRequerimiento'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    requerimientoId = db.Column(db.Integer, db.ForeignKey('TRequerimiento.id'), nullable=False)
    luchadorId = db.Column(db.Integer, db.ForeignKey('TUser.id'), nullable=False)
    torneoId = db.Column(db.Integer, db.ForeignKey('TTorneo.id'), nullable=False)
    nota = db.Column(db.String(255), nullable=False)
    Eliminado = db.Column(db.Boolean, default=False)
    Activo = db.Column(db.Boolean, default=True)
    luchador = db.relationship('TUser', backref='notaRequerimientoLuchador', lazy=True)
    requerimiento = db.relationship('TRequerimiento', backref='notaRequerimientoRequerimiento', lazy=True)
    torneo = db.relationship('TTorneo', backref='notaRequerimientoTorneo', lazy=True)
    
    def __init__(self, requeriemientoId, luchadorId, torneoId, nota, Eliminado=False, Activo=True):
        self.requeriemientoId = requeriemientoId 
        self.luchadorId = luchadorId 
        self.torneoId = torneoId 
        self.nota = nota
        self.Eliminado = Eliminado
        self.Activo = Activo
    def __repr__(self):
        return '<TNotaRequerimiento %r>' % self.id
    def serialize(self):
        return {
            'id': self.id,
            'requeriemientoId': self.requeriemientoId,
            'luchadorId': self.luchadorId,
            'torneoId': self.torneoId,
            'nota': self.nota,
            'Eliminado': self.Eliminado,
            'Activo': self.Activo
        }
   