from flask import Flask
# instalar flask_cors con pip install flask_cors
from flask_cors import CORS
from app.Infraestructure.db import db
from dotenv import load_dotenv
import os
from flasgger import Swagger

load_dotenv()

def create_app():
    app = Flask(__name__)
    print(os.environ.get('SQLALCHEMY_DATABASE_URI'))
    CORS(app)
    Swagger(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    db.init_app(app)
    return app
