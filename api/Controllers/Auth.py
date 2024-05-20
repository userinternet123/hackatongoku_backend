from flask import request, jsonify
from flask_jwt_extended import create_access_token
from api.models import TUser 
from flask_restful import Resource

class AuthController(Resource):
    
    def post(self):
        print('ingresa a post Auth')
        username = request.json.get("username", None)
        password = request.json.get("password", None)
        user = TUser.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            return {"msg": "Bad username or password"}, 401
        access_token = create_access_token(identity=user.id)
        
        return jsonify({"token": access_token,"user_id":user.id})