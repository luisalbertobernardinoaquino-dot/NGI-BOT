from flask import Flask, request, render_template_string

app = Flask(__name__)

def responder(pregunta):
    pregunta = pregunta.lower()

    if "triste" in pregunta:
        return "📖 Salmo 34:18<br><br><b>Interpretación:</b> Dios está cerca de los que tienen el corazón quebrantado. No estás solo; este momento puede ser una oportunidad para buscar consuelo, oración y esperanza."

    elif "miedo" in pregunta or "temor" in pregunta:
        return "📖 Isaías 41:10<br><br><b>Interpretación:</b> Dios recuerda que no debes vivir dominado por el temor, porque Él promete fortaleza, ayuda y compañía."

    elif "ansiedad" in pregunta or "preocupado" in pregunta:
        return "📖 Filipenses 4:6-7<br><br><b>Interpretación:</b> La Biblia enseña a presentar nuestras cargas a Dios en oración, confiando en que su paz puede guardar el corazón."

    elif "solo" in pregunta or "soledad" in pregunta:
        return "📖 Deuteronomio 31:8<br><br><b>Interpretación:</b> Dios promete ir delante de ti y no abandonarte. La soledad no significa ausencia de propósito."

    elif "gracias" in pregunta or "agradecido" in pregunta:
        return "📖 1 Tesalonicenses 5:18<br><br><b>Interpretación:</b> La gratitud fortalece la fe y permite reconocer la presencia de Dios aun en los procesos difíciles."

    else:
        return "📖 Salmo 119:105<br><br><b>Interpretación:</b> La Palabra de Dios puede ser una lámpara para tus pasos. Comparte cómo te sientes y buscaré una cita bíblica que te oriente."

html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>NGI-BOT</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            font-family: Arial, sans-serif;
            background:
                linear-gradient(rgba(255,255,255,0.86), rgba(255,255,255,0.90)),
                url("/static/images/fondo.png");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: #11324d;
        }

        .container {
            width: 92%;
            max-width: 900px;
            margin: auto;
            padding: 20px 0;
        }

        .header {
            text-align: center;
            animation: fadeDown 1s ease;
        }

        .header-box {
            max-height: 20vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }

        .logo {
            width: 95px;
            max-width: 20vw;
            border-radius: 50%;
            filter: drop-shadow(0 6px 12px rgba(0,70,140,0.25));
        }

        .church-name {
            margin-top: 6px;
            font-size: 0.9rem;
            font-weight: bold;
            color: #006fae;
        }

        h1 {
            margin: 14px 0 5px;
            font-size: 2.3rem;
            color: #0077b6;
        }

        .subtitle {
            margin: 0 0 15px;
            font-size: 1rem;
            color: #31566f;
        }

        .welcome-card {
            position: relative;
            background: rgba(255,255,255,0.88);
            border: 1px solid rgba(0,119,182,0.20);
            border-radius: 22px;
            padding: 18px;
            margin: 15px auto;
            max-width: 620px;
            box-shadow: 0 12px 30px rgba(0,90,150,0.16);
            text-align: center;
            animation: floatIn 1s ease;
        }

        .close-welcome {
            position: absolute;
            top: 8px;
            right: 12px;
            border: none;
            background: transparent;
            font-size: 22px;
            cursor: pointer;
            color: #0077b6;
        }

        .dove-area {
            position: relative;
            width: 150px;
            height: 130px;
            margin: auto;
        }

        .cross {
            position: absolute;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            font-size: 34px;
            color: #d4af37;
            text-shadow: 0 0 12px rgba(212,175,55,0.8);
            animation: glow 2s infinite alternate;
        }

        .dove {
            width: 110px;
            margin-top: 26px;
            animation: fly 2.2s ease-in-out infinite;
            filter: drop-shadow(0 0 16px rgba(255,220,120,0.8));
        }

        .welcome-text {
            font-size: 1rem;
            line-height: 1.5;
            color: #24465c;
        }

        .chat-box {
            background: rgba(255,255,255,0.92);
            border-radius: 24px;
            box-shadow: 0 16px 40px rgba(0,80,140,0.18);
            overflow: hidden;
            border: 1px solid rgba(0,119,182,0.20);
            animation: fadeUp 1s ease;
        }

        .messages {
            height: 390px;
            overflow-y: auto;
            padding: 20px;
        }

        .bubble {
            max-width: 78%;
            padding: 13px 16px;
            margin-bottom: 14px;
            border-radius: 18px;
            line-height: 1.5;
            animation: pop 0.35s ease;
        }

        .user {
            margin-left: auto;
            background: #0077b6;
            color: white;
            border-bottom-right-radius: 4px;
        }

        .bot {
            margin-right: auto;
            background: #eef8ff;
            color: #11324d;
            border-bottom-left-radius: 4px;
            border: 1px solid #cbeeff;
        }

        .typing {
            display: none;
            padding: 0 20px 15px;
            color: #0077b6;
            font-size: 0.9rem;
            font-style: italic;
        }

        form {
            display: flex;
            gap: 10px;
            padding: 16px;
            background: rgba(238,248,255,0.95);
            border-top: 1px solid rgba(0,119,182,0.18);
        }

        input {
            flex: 1;
            padding: 14px 16px;
            border-radius: 18px;
            border: 1px solid #b8e4f8;
            font-size: 1rem;
            outline: none;
        }

        input:focus {
            border-color: #0077b6;
            box-shadow: 0 0 0 3px rgba(0,119,182,0.12);
        }

        button.send {
            border: none;
            border-radius: 18px;
            padding: 0 24px;
            background: linear-gradient(135deg, #0096c7, #006fae);
            color: white;
            font-weight: bold;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
        }

        button.send:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 18px rgba(0,119,182,0.35);
        }

        @keyframes fadeDown {
            from { opacity: 0; transform: translateY(-18px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(18px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes floatIn {
            from { opacity: 0; transform: scale(0.96); }
            to { opacity: 1; transform: scale(1); }
        }

        @keyframes pop {
            from { opacity: 0; transform: scale(0.96); }
            to { opacity: 1; transform: scale(1); }
        }

        @keyframes fly {
            0%, 100% { transform: translateY(0) scale(1) rotate(0deg); }
            50% { transform: translateY(-10px) scale(1.04) rotate(1deg); }
        }

        @keyframes glow {
            from { opacity: 0.65; }
            to { opacity: 1; }
        }

        @media (max-width: 600px) {
            h1 {
                font-size: 1.8rem;
            }

            .subtitle {
                font-size: 0.9rem;
            }

            .messages {
                height: 360px;
            }

            .bubble {
                max-width: 92%;
                font-size: 0.95rem;
            }

            form {
                flex-direction: column;
            }

            button.send {
                padding: 14px;
            }

            .logo {
                width: 75px;
            }
        }
    </style>
</head>

<body>
    <div class="container">

        <div class="header">
            <div class="header-box">
                <img src="/static/images/logo.png" class="logo">
                <div class="church-name">NGI Iglesia Cristiana Nueva Generación Internacional</div>
            </div>

            <h1>NGI-BOT</h1>
            <p class="subtitle">Este BOT te refiere citas bíblicas que son guía en tu proceso</p>
        </div>

        <div class="welcome-card" id="welcomeCard">
            <button class="close-welcome" onclick="cerrarBienvenida()">×</button>
            <div class="dove-area">
                <div class="cross">✝</div>
                <img src="/static/images/ES.png" class="dove">
            </div>
            <div class="welcome-text">
                Bienvenido. Soy <b>NGI-BOT</b>. Cuéntame cómo te sientes y te compartiré una cita bíblica como guía espiritual.
            </div>
        </div>

        <div class="chat-box">
            <div class="messages" id="messages">
                {% if pregunta %}
                    <div class="bubble user">{{ pregunta }}</div>
                    <div class="bubble bot">{{ respuesta|safe }}</div>
                {% else %}
                    <div class="bubble bot">
                        Hola, soy <b>NGI-BOT</b>. Escribe tu estado de ánimo, por ejemplo: tristeza, miedo, ansiedad, soledad o gratitud.
                    </div>
                {% endif %}
            </div>

            <div class="typing" id="typing">NGI-BOT está escribiendo...</div>

            <form method="POST" onsubmit="mostrarEscribiendo()">
                <input type="text" name="pregunta" placeholder="Escribe cómo te sientes..." required>
                <button class="send" type="submit">Enviar</button>
            </form>
        </div>

    </div>

    <script>
        function cerrarBienvenida() {
            const card = document.getElementById("welcomeCard");
            card.style.opacity = "0";
            card.style.transform = "scale(0.95)";
            setTimeout(() => {
                card.style.display = "none";
            }, 300);
        }

        function mostrarEscribiendo() {
            document.getElementById("typing").style.display = "block";
        }

        const messages = document.getElementById("messages");
        messages.scrollTop = messages.scrollHeight;
    </script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    pregunta = ""
    respuesta = ""

    if request.method == "POST":
        pregunta = request.form.get("pregunta", "")
        respuesta = responder(pregunta)

    return render_template_string(html, pregunta=pregunta, respuesta=respuesta)

if __name__ == "__main__":
    app.run(debug=True)
