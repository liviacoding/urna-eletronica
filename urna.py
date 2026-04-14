from flask import Flask , render_template, request

app = Flask(__name__)

votos = {"Maria": 0, "Joao": 0, "AnaJulia": 0}


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/votar", methods=["POST"])
def votar():
    voto = request.form.get("voto_usuario")

    if voto == "1":
        votos["Maria"] += 1
    elif voto == "2":
        votos["Joao"] += 1
    elif voto == "3":
        votos["AnaJulia"] += 1
    elif voto == "0":
        return render_template("encerramento.html")    
    else:
        return render_template("index.html",erro="Número Inválido! Tente novamente.")    
    
    return render_template("Resultado.html", Maria=votos["Maria"], AnaJulia=votos["AnaJulia"], Joao=votos["Joao"])

    
if __name__ == "__main__":
    app.run(debug=True)
