from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class TUser(db.Model):
    __tablename__ = 'TUser'
    # colocar privado el password
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userName = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    imagen = db.Column(db.String(255), nullable=True)
    Eliminado = db.Column(db.Boolean, nullable=False, default=False)
    Activo = db.Column(db.Boolean, nullable=False, default=True)
    inscripcion = db.relationship('TInscripcion', backref='userInscripciones', lazy=True)
    notaRequerimiento = db.relationship('TNotaRequerimiento', backref='userNotaRequerimiento', lazy=True)
    
    def __init__(self, name, email, password, imagen=None, Eliminado=False, Activo=True):
        self.userName = name
        self.email = email
        self.password = generate_password_hash(password)
        self.imagen = imagen
        self.Eliminado = Eliminado
        self.Activo = Activo
        #self.password = password
    def __repr__(self):
        return '<TUser %r>' % self.id
    def check_password(self, password):
        return check_password_hash(self.password, password)
    def encrypt_password(self, password):
        self.password = generate_password_hash(password)
        return generate_password_hash(password)
    def serialize(self):
        return {
            'id': self.id,
            'userName': self.userName,
            'email': self.email,
            'imagen': self.imagen,
            'Eliminado': self.Eliminado,
            'Activo': self.Activo
        }