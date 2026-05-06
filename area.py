from flask import Flask, render_template

restrito = Flask(__name__)

@restrito.route('/arearestrita/<chave>')
def mostrar_cadeado(chave):
    if chave == "1":
        imagem_escolhida = "cadeado_fechado.png"
    elif chave == "2":
        imagem_escolhida = "cadeado_aberto.png"
    else:
        imagem_escolhida = None
    return render_template("area.html", simbolo=imagem_escolhida)

if __name__ == "__main__":
    restrito.run(debug=True)
