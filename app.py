from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

@app.route('/')
def inicio():
    nome = request.cookies.get('nome_usuario', '')
    tema = request.cookies.get('tema', 'claro')
    return render_template('inicio.html', nome=nome, tema=tema)

@app.route('/salvar-nome', methods=['POST'])
def salvar_nome():
    nome = request.form.get('nome', '').strip()
    resposta = make_response(redirect(url_for('inicio')))
    if nome:
        resposta.set_cookie('nome_usuario', nome, max_age=60*60*24*30)
    return resposta

@app.route('/alterar-tema', methods=['POST'])
def alterar_tema():
    tema_atual = request.cookies.get('tema', 'claro')
    novo_tema = 'escuro' if tema_atual == 'claro' else 'claro'
    resposta = make_response(redirect(url_for('inicio')))
    resposta.set_cookie('tema', novo_tema, max_age=60*60*24*30)
    return resposta

@app.route('/limpar')
def limpar():
    resposta = make_response(redirect(url_for('inicio')))
    resposta.delete_cookie('nome_usuario')
    resposta.delete_cookie('tema')
    return resposta

if __name__ == '__main__':
    app.run(debug=True)