"""Chatbot controller for NGI-BOT."""

from gemini_engine import generar_respuesta_gemini


def responder(pregunta):
    """Return an AI-generated Bible-oriented response."""
    if not pregunta or not pregunta.strip():
        return (
            "<b>REFERENCIA:</b> Salmo 119:105 (RVR1960)<br><br>"
            "<b>VERSÍCULO:</b> “Lámpara es a mis pies tu palabra, y lumbrera a mi camino.”<br><br>"
            "<b>REFLEXIÓN:</b> Comparte cómo te sientes y buscaré una orientación bíblica para ti."
        )

    return generar_respuesta_gemini(pregunta)
