from flask import Flask
from flask_cors import CORS
from app.config import Config
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_migrate import Migrate

# Create an instance of Flask
app = Flask(__name__)
# Load the config file
app.config.from_object(Config)
# CORS 
CORS(app, resources={r"/*/": {"origins": "*"}})
api = Api(app, version='1.0', title='API', description='A simple API')
# We put Swagger
Swagger(app)
# Database instance
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# APP Routes
from app.Presentation.UserController import api as user_ns
api.add_namespace(user_ns, path='/users')

