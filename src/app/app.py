from flask import Flask
from flask_cors import CORS
from app.config import Config
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy

# Crea una instancia de la aplicacion
app = Flask(__name__)
# Carga la configuracion de la aplicacion
app.config.from_object(Config)
# Habilita CORS
CORS(app)
# Habilita Swagger
Swagger(app)
# Crea una instancia de la base de datos
db = SQLAlchemy(app)
