from flask import Flask
from flask_cors import CORS
from app.config import Config
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_migrate import Migrate
from flask_injector import FlaskInjector

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
from app.Presentation.TaskController import api as task_ns
from app.Security.Auth import api as auth_ns
api.add_namespace(user_ns, path='/users')
api.add_namespace(task_ns, path='/tasks')
api.add_namespace(auth_ns, path='/auth')


# Dependency Injection
FlaskInjector(app=app)