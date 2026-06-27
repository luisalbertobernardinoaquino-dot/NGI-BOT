"""Rule-based response engine for NGI-BOT."""


def responder(pregunta):
    """Return the current Bible-based response for a user's message."""
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
