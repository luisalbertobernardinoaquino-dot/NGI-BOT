import os
import google.generativeai as genai

from prompt_system import PROMPT_SISTEMA


def generar_respuesta_gemini(pregunta):
    """Envía la pregunta del usuario a Gemini y devuelve una respuesta espiritual."""

    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        return (
            "<b>ERROR:</b> No se encontró la variable GEMINI_API_KEY.<br><br>"
            "Configúrala en Render antes de usar Gemini."
        )

    genai.configure(api_key=api_key)

    modelo = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
{PROMPT_SISTEMA}

Mensaje del usuario:
{pregunta}
"""

    try:
        respuesta = modelo.generate_content(prompt)
        return respuesta.text.replace("\n", "<br>")
    except Exception as e:
        return (
            "<b>ERROR:</b> No se pudo generar respuesta con Gemini.<br><br>"
            f"Detalle: {str(e)}"
        )