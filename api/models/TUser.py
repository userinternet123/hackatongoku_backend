from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class TUser(db.Model):
    __tablename__ = 'TUser'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    def __init__(self, name, email, password):
        self.username = name
        self.email = email
        self.password = generate_password_hash(password)
        #self.password = password
    def __repr__(self):
        return '<TUser %r>' % self.id
    def check_password(self, password):
        return check_password_hash(self.password, password)