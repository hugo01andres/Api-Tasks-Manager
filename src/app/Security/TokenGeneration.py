import jwt
from dotenv import load_dotenv
import os
from functools import wraps
from flask import request, jsonify

load_dotenv()

def generate_token(username):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    print(SECRET_KEY)
    token = jwt.encode({'username': username}, 'secret', algorithm='HS256')
    return token

def verify_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        try:
            data = jwt.decode(token, 'secret', algorithm='HS256')
            username = data['username']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token is expired'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token is invalid'}), 401
        return func(*args, **kwargs)
    return wrapper



