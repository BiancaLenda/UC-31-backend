from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("sobre.html")

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")

@app.route("/serviços")
def sobre():
    return render_template("serviços.html")

if __name__ == "__main__":
    app.run(debug=True)