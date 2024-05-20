from dotenv import load_dotenv
from flask import Flask
import os
from flask_cors import CORS
from flask_restful import Api
from api import Controllers as c
from api.models import db
from os.path import dirname, join
#from flask_jwt_extended import JWTManager
ENV = 'desa'
dotenv_path = ''
app = Flask(
    __name__,
    static_url_path='/statics',
    static_folder='./statics',
)

CORS(app)
if ENV == 'local':
    dotenv_path = join(dirname(__file__), '.env')
if ENV == 'desa':
    print('entra a desa', dirname(__file__))
    dotenv_path = join(dirname(__file__), '.env')
if ENV == 'qa':
    dotenv_path = join(dirname(__file__), '.env.qa')
if ENV == 'PRD':
    dotenv_path = join(dirname(__file__), '.env.prod')
print('inicia app')
print('dotenv_path', dotenv_path)
load_dotenv(dotenv_path)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
app.config['BUNDLE_ERRORS'] = os.getenv('BUNDLE_ERRORS')
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config["DEBUG"] = True #if ENV == 'local' else False
#app.config.from_object(Config())
db.init_app(app)
api = Api(app)

#app.config["JWT_SECRET_KEY"] = os.getenv('JWT_KEY')
#app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 86400
    #jwt = JWTManager(app)
    

@app.route('/api')
def home():

    return "ILU"

api.add_resource(c.PruebaApiController,
                 '/api/prueba/<int:id>','/api/prueba')



if __name__ == '__main__':
    app.run()