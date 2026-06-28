import os
from google import genai

from prompt_system import PROMPT_SISTEMA


def generar_respuesta_gemini(pregunta):
    """Envía la pregunta del usuario a Gemini y devuelve una respuesta espiritual."""

    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        return (
            "<b>ERROR:</b> No se encontró la variable GEMINI_API_KEY.<br><br>"
            "Configúrala en Render antes de usar Gemini."
        )

    try:
        client = genai.Client(api_key=api_key)

        prompt = f"""
{PROMPT_SISTEMA}

Mensaje del usuario:
{pregunta}
"""

        respuesta = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        texto = respuesta.text.strip()
        texto = texto.replace("**", "")
        texto = texto.replace("\n\n\n", "\n\n")
        texto = texto.replace("\n", "<br>")

        return texto

    except Exception as e:
        return (
            "<b>ERROR:</b> No se pudo generar respuesta con Gemini.<br><br>"
            f"Detalle: {str(e)}"
        )