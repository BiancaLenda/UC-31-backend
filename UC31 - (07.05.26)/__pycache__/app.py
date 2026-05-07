from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Bem-vinda!</h1>
    <p>Use /filme/acao, /filme/comedia ou /filme/terror para ver os gêneros disponíveis.</p>
    """


@app.route('/filme/<genero>')
def filme(genero):
    generos = {
        
        "acao": {
            "nome": "Ação",
            "imagem": "https://i.pinimg.com/1200x/22/a6/a4/22a6a48ea48d3c710fa15beb47f1db77.jpg",
            "descricao": "Filmes de ação que geram animação."
        },
        "comedia": {
            "nome": "Comédia",
            "imagem": "https://i.pinimg.com/736x/17/14/66/171466c26f59e5aa3e44a3d254f602d8.jpg",
            "descricao": "Filmes de comédia que te anima com ideias."
        },
        "terror": {
            "nome": "Terror",
            "imagem": "https://i.pinimg.com/webp85/1200x/99/44/6e/99446e4f76c26f773f1a3b89ecde7b38.webp",
            "descricao": "Filmes de terror que faz você chorar de horror."
        }
    }

    if genero in generos:
        return render_template("filme.html", genero=generos[genero])
    else:
        return "<h1>Gênero não disponível</h1>"

if __name__ == "__main__":
    app.run(debug=True)
