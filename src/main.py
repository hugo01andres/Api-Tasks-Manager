from app.app import app
from flask import redirect


# Ruta de inicio
@app.route('/')
def index():
    return redirect('/apidocs')

# Inicia la aplicacion
app = app