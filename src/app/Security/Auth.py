from app.app import db
from app.Models.User import User
from flask_restx import Resource, Namespace, ValidationError, fields
from app.Presentation.Resources.TokenResource import token_resource
from injector import inject
from app.Security.TokenTools import generate_token
import jwt

api = Namespace('auth', description='Auth related operations')

GenerateToken, Token = token_resource(api)


@api.route('/login')
class Auth(Resource):
    @inject
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @api.doc('Login')
    @api.expect(GenerateToken)
    @api.marshal_with(Token)
    def post(self):
        username = api.payload['username']
        password = api.payload['password']
        user = db.session.query(User).filter(User.username == username).first()
        if user is None:
            return {'token': 'Invalid username'}, 401
            
        if user.password == password:
            payload = {
                'user_id': user.id
            }
            token = generate_token(payload)
            return {"token": token} , 200
        else:
             return {'token': 'Invalid password'}, 401
            