from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    nome = "Baptysta"
    return render_template('contato.html', usuario=None, nome=nome, title="Home")

@app.route("/contato")
def home():
    return render_template('contato.html')

@app.route('/usuario')
def usuario():
    usuario = {'nome': 'Alba', 'sobrenome': 'Lopes'}
    return render_template('index.html', title='Página Inicial', usuario=usuario)

@app.route('/dados', defaults={"nome":"usuário comum"}) 
@app.route('/dados/<nome>')
def dados(nome):
    return f'Olá, {nome}'

@app.route('/semestre/<int:x>')
def semestre(x):
    return 'Estamos no semestre ' + str(x)

@app.route('/pagamento/<float:valor>')
def pagamento(valor):
    return 'Você pagou: '+ str(valor)

@app.route('/arearestrita/<int:id>')
def arearestrita(id):
    if id == 1:
        return "[cadeado fechado] Acesso bloqueado"
    else:
        return "[cadeado aberto] Acesso liberado"
    
@app.route('/operacao/<tipo>/<float:n1>/<float:n2>')
def operacao(tipo, n1, n2):
    if tipo == 'Soma':
        resultado = n1 + n2
    elif tipo == 'Subtração':
        resultado = n1 - n2
    elif tipo == 'Divisão':
        resultado = n1 / n2
    else:
        resultado = n1 * n2

    return str(resultado)
    
#Questão 1

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f'Greetings, {nome}'

#Questão 2
@app.route('/calculo/<n1>/<n2>')
def soma(n1, n2):
    resultado = n1 + n2
    return resultado

#Questão 3
@app.route('/idade/<nome>/<int:idade>')
def verificar_idade(nome, idade):
    if idade <= 18:
        return f"Olá {nome} Você é de menor"
    else:
        return "Você é de maior"

@app.route('/pizzaria/<sabor>')
def pizza(sabor):
    if sabor == 'calabresa':
        return render_template('calabresa.html', title='Calabresa Acebolada')
    
    elif sabor == 'marguerita':
        return render_template('marguerita.html', title='Marguerita Especial')
    
    elif sabor == 'frango':
        return render_template('frango.html', title='Frango com Catupiry')
    
    else:
        return "<h1>Sabor não encontrado!</h1><p>Consulte nosso cardápio.</p>", 404
    
@app.route('/delivery/<service>')
def delivery(service):
    if service == 'inicio':
        return render_template('inicio.html', title='Inicio - Come e Come')
    
    elif service == 'cardapio':
        return render_template('cardapio.html', title='Calabresa Acebolada')
    
    elif service == 'pedido':
        return render_template('pedido.html', title='Calabresa Acebolada')
    
    elif service == 'contato':
        return render_template('contator.html', title='Calabresa Acebolada')
    
    else:
         return "<h1>página não encontrado!</h1>", 404


if __name__ == "__main__":
    app.run(debug=True)
