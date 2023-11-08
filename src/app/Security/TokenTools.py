import jwt
from dotenv import load_dotenv
import os
from functools import wraps
from flask import request, jsonify, g

load_dotenv()

def generate_token(data):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    token = jwt.encode({'user_id': data['user_id']}, SECRET_KEY, algorithm='HS256')
    return token

def token_required(func):
    def wrapper(*args, **kwargs):
        # Aquí verificarías el token de autenticación
        SECRET_KEY = os.environ.get('SECRET_KEY')
        token_with_Bearer = request.headers.get('Authorization')
        if token_with_Bearer == None:
            return {'message': 'Token is missing'}, 401
        print(token_with_Bearer)
        split_token = token_with_Bearer.split(' ')
        token = split_token[1]
        print(token)
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except:
            return {'message': 'Token is invalid'}, 401
        
        return func(*args, **kwargs)
    return wrapper


def g_tokens(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers['Authorization'].replace('Bearer ', '',1)
        if token:
            decoded_token = jwt.decode(token, os.environ.get('SECRET_KEY'), algorithms=["HS256"])
            g.user_id = decoded_token['user_id']
        else:
            g.user_id = None
        return f(*args, **kwargs)
    return decorated





