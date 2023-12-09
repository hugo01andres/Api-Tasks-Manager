from app.app import app
from flask import redirect


# Ruta de inicio
@app.route('/')
def index():
    return redirect('/apidocs')

# Inicia la aplicacion
if __name__ == '__main__':
    app.run(port=5000, debug=True)