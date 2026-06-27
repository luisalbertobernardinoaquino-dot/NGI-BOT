from flask import Flask, render_template, request

from chatbot import responder


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    pregunta = ""
    respuesta = ""

    if request.method == "POST":
        pregunta = request.form.get("pregunta", "")
        respuesta = responder(pregunta)

    return render_template(
        "index.html",
        pregunta=pregunta,
        respuesta=respuesta,
    )


if __name__ == "__main__":
    app.run(debug=True)
