from flask import Flask, jsonify, request, render_template
import secrets
import string

app = Flask(__name__)


def generar_password(length=16, numbers=True, symbols=True):

    letras = string.ascii_letters
    numeros = string.digits if numbers else ""
    simbolos = "!@#$%^&*()_+-=" if symbols else ""

    caracteres = letras + numeros + simbolos

    password = "".join(
        secrets.choice(caracteres) for _ in range(length)
    )

    return password


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/api/password")
def api_password():

    length = int(request.args.get("length", 16))
    numbers = request.args.get("numbers", "true") == "true"
    symbols = request.args.get("symbols", "true") == "true"

    password = generar_password(length, numbers, symbols)

    return jsonify(
        {
            "password": password,
            "length": length,
            "numbers": numbers,
            "symbols": symbols,
        }
    )


if __name__ == "__main__":

    app.run(debug=True)