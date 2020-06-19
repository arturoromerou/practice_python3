from flask import Flask
from flask import render_template # libreria que renderiza los templates


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

"""en esta ruta le mandamos variables a nuestro template"""
@app.route('/user/<name>')
def user(name='Arturo'):
    age = 19
    my_list = [1, 2, 3, 4, 5, 6]
    return render_template('user.html', nombre=name, age=age, list=my_list)


if __name__ == '__main__':
    app.run