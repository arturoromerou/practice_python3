from flask import Flask
from flask import render_template # libreria que renderiza los templates


app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return render_template('index.html')

if __name__ == '__main__':
    app.run