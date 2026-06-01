from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    aviso = ""

    if request.method == 'POST':
        gamer_tag = request.form.get('gamer_tag')
        titulo = request.form.get('titulo')
        contato = request.form.get('contato')

        if not gamer_tag or not titulo or not contato:
            aviso = "Todos os campos devem ser preenchidos."
        elif len(gamer_tag) < 4:
            aviso = "A gamer tag precisa ter pelo menos 4 caracteres."
        else:
            aviso = "Cadastro concluído com sucesso!"

    return render_template('cadastro1.html', aviso=aviso)

if __name__ == "__main__":
    app.run(debug=True)

