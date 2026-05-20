from flask import Flask, render_template
from flask import Flask, request

app = Flask(__name__)

@app.route('/autenticar')
def autenticar():
    return render_template('formulario.html')

@app.route('/autenticar', methods = ['GET'])
def autenticar():
    usuario = request.args.get('usuario')
    senha = request.args.get('senha')
    return "{} e {}".format(usuario, senha)

if __name__ == '__main__':
    app.run(debug=True)