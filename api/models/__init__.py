from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .TPrueba import TPrueba
from .TUser import TUser
from .TCategoria import TCategoria
from .TCategoriaRequerimiento import TCategoriaRequerimiento
from .TRequerimiento import TRequerimiento
from .TInscripcion import TInscripcion
from .TNotaRequerimiento import TNotaRequerimiento
from .TTorneo import TTorneo
from .TTorneoCategoria import TTorneoCategoria 
