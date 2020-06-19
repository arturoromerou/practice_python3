from flask import Flask # importamos flask
from flask import request # nos ayuda a recibir parametros desde la url

app = Flask(__name__) # nuevo objeto

@app.route('/') # wrap o decorador
def index():
    return "hola mundo"

# creamos una ruta nueva llamada params
@app.route('/params')
def params():
    """funcion que nos permite recibir parametros desde la url y puede recibir mas de 1 param"""
    param = request.args.get('params1', 'no contiene parametro.')
    return 'el parametro es: {}'.format(param)

# creamos una ruta que recibe un parametro name desde la url
@app.route('/params/') # en caso de que no se reciba un parametro igual ejecutar params
@app.route('/params/<name>/<int:num>') # obligamos a que en la ruta sea un int la variable num
def user(name = 'este es un valor por default', num = 'nada'):
    """esta funcion recibe el parametro de la url y lo muetra en pantalla"""
    return 'el parametro es: {} {}'.format(name, num)

if __name__ == '__main__':
    app.run # se encarga de ejecutar el servidor por defecto en el puerto 5000