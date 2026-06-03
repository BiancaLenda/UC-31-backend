from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('Nome', '').strip().title()
        email = request.form.get('Email','').strip().lower()
        telefone = request.form.get('Telefone','').strip().replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
        cpf = request.form.get('CPF','').strip().replace(".", "").replace("-", "")
        cidade = request.form.get('Cidade','').strip().title()
        estado = request.form.get('Estado','').strip().upper()
        curso = request.form.get('Curso','').strip().title()
        idade = request.form.get('Idade','').strip()
        senha = request.form.get('Senha','').strip()
     
        erros = []
        if len(nome) < 8: 
            erros.append("Nome inválido.")
        if "@" not in email or ".com" not in email: 
            erros.append("E-mail inválido.")
        if not telefone.isdigit() or len(telefone) != 11: 
            erros.append("Telefone inválido.")
        if not cpf.isdigit() or len(cpf) != 11: 
            erros.append("CPF inválido.")
        if len(cidade) < 3: 
            erros.append("Cidade inválida.")
        if len(estado) != 2: 
            erros.append("Estado inválido.")
        if curso == "": 
            erros.append("Curso inválido.")
        if not idade.isdigit() or int(idade) < 16: 
            erros.append("Idade inválida.")
        if len(senha) < 8 or not any(char.isdigit() for char in senha): 
            erros.append("Senha muito fraca.")

        if erros:
            return "<br>".join(erros)
        else:
            return f"""
            <h2>Cadastro realizado com sucesso!</h2>
            Nome: {nome}<br>
            E-mail: {email}<br>
            Telefone: {telefone}<br>
            CPF: {cpf}<br>
            Cidade: {cidade}<br>
            Estado: {estado}<br>
            Curso: {curso}<br>
            Idade: {idade}<br>
            """

if __name__ == '__main__':
    app.run(debug=True)
