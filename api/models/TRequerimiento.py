from . import db

class TRequerimiento(db.Model):
    __tablename__ = 'TRequerimiento'
    #__table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descripcion  = db.Column(db.String(255), nullable=False)
    Eliminado = db.Column(db.Boolean, default=False)
    Activo = db.Column(db.Boolean, default=True)
    categoriaRequerimiento = db.relationship('TCategoriaRequerimiento', backref='requerimientoCategoriaRequerimiento', lazy=True)
    notaRequerimiento = db.relationship('TNotaRequerimiento', backref='requerimientoNotaRequerimiento', lazy=True)
    
    def __init__(self, descripcion, Eliminado=False, Activo=True):
        self.descripcion = descripcion
        self.Eliminado = Eliminado
        self.Activo = Activo
        
    def __repr__(self):
        return '<TRequerimiento %r>' % self.id
    def serialize(self):
        return {
            'id': self.id,
            'descripcion': self.descripcion,
            'Eliminado': self.Eliminado,
            'Activo': self.Activo
        }