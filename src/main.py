from app.app import create_app
from app.Infraestructure.db import db
from flask import redirect

# Crea una instancia de la aplicacion de flask
app = create_app()

# Crea las tablas de la base de datos
with app.app_context():
    db.create_all()

# Ruta de inicio
@app.route('/')
def index():
    return redirect('/apidocs')

# Inicia la aplicacion
if __name__ == '__main__':
    app.run(port=5000, debug=True)