from . import db

class TPrueba(db.Model):
    __tablename__ = 'Tprueba'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #fecha = db.Column(db.DateTime)
    #valor = db.Column(db.Float)
    descripcion = db.Column(db.String(255))
    def __init__(self, descripcion, fecha=None, valor=None):
        #self.fecha = fecha
        #self.valor = valor
        self.descripcion = descripcion
    def __repr__(self):
        return '<Tprueba %r>' % self.id