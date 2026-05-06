from flask import Flask, render_template

calculadora = Flask(__name__)

@calculadora.route('/operacao/<acao>/<primeiro>/<segundo>')
def executar_operacao(acao, primeiro, segundo):
    dado1 = float(primeiro)
    dado2 = float(segundo)

    if acao == "sum":
        resposta = dado1 + dado2
    elif acao == "sub":
        resposta = dado1 - dado2
    elif acao == "mult":
        resposta = dado1 * dado2
    elif acao == "div":
        if dado2 != 0:
            resposta = dado1 / dado2
        else:
            resposta = "Erro: divisão por zero"
    else:
        resposta = "Operação inválida"

    return render_template("operador.html", resultado=resposta)

if __name__ == "__main__":
    calculadora.run(debug=True)
