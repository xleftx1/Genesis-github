from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")
@app.route("/corte")
def corte():
    return render_template("corte.html")

@app.route("/tinturado")
def tinturado():
    return render_template("tinturado.html")

@app.route("/peinado")
def peinado():
    return render_template("peinado.html")

if __name__ == "__main__":
    app.run(debug=True);