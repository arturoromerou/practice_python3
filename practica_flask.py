from flask import Flask

app = Flask(__name__) # nuevo objeto

@app.route('/') # wrap o decorador
def index():
    return "hola mundo"

app.run # se encarga de ejecutar el servidor por defecto en el puerto 5000