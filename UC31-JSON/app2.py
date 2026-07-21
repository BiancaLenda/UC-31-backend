from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

app = Flask(__name__)
app.secret_key = "chave-secreta-biblioteca"

ARQUIVO_JSON = "livro.json"


def carregar_livros():
    """Lê o arquivo JSON e retorna a lista de livros.
    Caso o arquivo não exista, cria automaticamente com uma lista vazia."""
    if not os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
            json.dump([], arquivo, ensure_ascii=False, indent=4)
        return []

    with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return []


def salvar_livros(livros):
    """Salva a lista de livros no arquivo JSON."""
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(livros, arquivo, ensure_ascii=False, indent=4)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        autor = request.form.get("autor", "").strip()
        ano = request.form.get("ano", "").strip()
        categoria = request.form.get("categoria", "").strip()
        quantidade = request.form.get("quantidade", "").strip()

        # Validação: campos vazios
        if not titulo or not autor or not ano or not categoria or not quantidade:
            flash("Todos os campos devem ser preenchidos.", "erro")
            return redirect(url_for("index"))

        # Validação: ano apenas números
        if not ano.isdigit():
            flash("O ano deve conter apenas números.", "erro")
            return redirect(url_for("index"))

        # Validação: quantidade inteira maior que zero
        if not quantidade.isdigit() or int(quantidade) <= 0:
            flash("A quantidade deve ser um número inteiro maior que zero.", "erro")
            return redirect(url_for("index"))

        livros = carregar_livros()

        novo_livro = {
            "titulo": titulo,
            "autor": autor,
            "ano": int(ano),
            "categoria": categoria,
            "quantidade": int(quantidade),
        }

        livros.append(novo_livro)
        salvar_livros(livros)

        flash("Livro cadastrado com sucesso!", "sucesso")
        return redirect(url_for("listar_livros"))

    return render_template("cadastro.html")

@app.route("/livros")
def listar_livros():
    livros = carregar_livros()
    return render_template("livros.html", livros=livros)

@app.route("/buscar", methods=["GET", "POST"])
def buscar_livro():
    resultado = None
    buscado = False

    if request.method == "POST":
        titulo_busca = request.form.get("titulo", "").strip().lower()
        buscado = True

        if titulo_busca:
            livros = carregar_livros()
            for livro in livros:
                if livro["titulo"].strip().lower() == titulo_busca:
                    resultado = livro
                    break

    return render_template("buscar.html", resultado=resultado, buscado=buscado)

@app.route("/editar/<int:indice>", methods=["GET", "POST"])
def editar_livro(indice):
    livros = carregar_livros()

    if indice < 0 or indice >= len(livros):
        flash("Livro não encontrado.", "erro")
        return redirect(url_for("listar_livros"))

    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        autor = request.form.get("autor", "").strip()
        ano = request.form.get("ano", "").strip()
        categoria = request.form.get("categoria", "").strip()
        quantidade = request.form.get("quantidade", "").strip()

        if not titulo or not autor or not ano or not categoria or not quantidade:
            flash("Todos os campos devem ser preenchidos.", "erro")
            return redirect(url_for("editar_livro", indice=indice))

        if not ano.isdigit():
            flash("O ano deve conter apenas números.", "erro")
            return redirect(url_for("editar_livro", indice=indice))

        if not quantidade.isdigit() or int(quantidade) <= 0:
            flash("A quantidade deve ser um número inteiro maior que zero.", "erro")
            return redirect(url_for("editar_livro", indice=indice))

        livros[indice] = {
            "titulo": titulo,
            "autor": autor,
            "ano": int(ano),
            "categoria": categoria,
            "quantidade": int(quantidade),
        }

        salvar_livros(livros)
        flash("Livro atualizado com sucesso!", "sucesso")
        return redirect(url_for("listar_livros"))

    livro = livros[indice]
    return render_template("editar.html", livro=livro, indice=indice)

@app.route("/excluir/<int:indice>")
def excluir_livro(indice):
    livros = carregar_livros()

    if 0 <= indice < len(livros):
        livros.pop(indice)
        salvar_livros(livros)
        flash("Livro excluído com sucesso!", "sucesso")
    else:
        flash("Livro não encontrado.", "erro")

    return redirect(url_for("listar_livros"))


if __name__ == "__main__":
    app.run(debug=True)