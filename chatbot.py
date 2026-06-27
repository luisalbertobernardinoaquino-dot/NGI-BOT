"""Rule-based response engine for NGI-BOT."""


def crear_respuesta(referencia, versiculo, reflexion):
    """Build a response with the three fields required by the UI."""
    return (
        f"<b>REFERENCIA:</b> {referencia}<br><br>"
        f"<b>VERSÍCULO:</b> {versiculo}<br><br>"
        f"<b>REFLEXIÓN:</b> {reflexion}"
    )


def responder(pregunta):
    """Return the current Bible-based response for a user's message."""
    pregunta = pregunta.lower()

    if "triste" in pregunta:
        return crear_respuesta(
            "Salmo 34:18 (RVR1960)",
            "“Cercano está Jehová a los quebrantados de corazón; y salva a los contritos de espíritu.”",
            "Dios está cerca de los que tienen el corazón quebrantado. No estás solo; este momento puede ser una oportunidad para buscar consuelo, oración y esperanza.",
        )

    elif "miedo" in pregunta or "temor" in pregunta:
        return crear_respuesta(
            "Isaías 41:10 (RVR1960)",
            "“No temas, porque yo estoy contigo; no desmayes, porque yo soy tu Dios que te esfuerzo; siempre te ayudaré, siempre te sustentaré con la diestra de mi justicia.”",
            "Dios recuerda que no debes vivir dominado por el temor, porque Él promete fortaleza, ayuda y compañía.",
        )

    elif "ansiedad" in pregunta or "preocupado" in pregunta:
        return crear_respuesta(
            "Filipenses 4:6-7 (RVR1960)",
            "“Por nada estéis afanosos, sino sean conocidas vuestras peticiones delante de Dios en toda oración y ruego, con acción de gracias. Y la paz de Dios, que sobrepasa todo entendimiento, guardará vuestros corazones y vuestros pensamientos en Cristo Jesús.”",
            "La Biblia enseña a presentar nuestras cargas a Dios en oración, confiando en que su paz puede guardar el corazón.",
        )

    elif "solo" in pregunta or "soledad" in pregunta:
        return crear_respuesta(
            "Deuteronomio 31:8 (RVR1960)",
            "“Y Jehová va delante de ti; él estará contigo, no te dejará, ni te desamparará; no temas ni te intimides.”",
            "Dios promete ir delante de ti y no abandonarte. La soledad no significa ausencia de propósito.",
        )

    elif "gracias" in pregunta or "agradecido" in pregunta:
        return crear_respuesta(
            "1 Tesalonicenses 5:18 (RVR1960)",
            "“Dad gracias en todo, porque esta es la voluntad de Dios para con vosotros en Cristo Jesús.”",
            "La gratitud fortalece la fe y permite reconocer la presencia de Dios aun en los procesos difíciles.",
        )

    else:
        return crear_respuesta(
            "Salmo 119:105 (RVR1960)",
            "“Lámpara es a mis pies tu palabra, y lumbrera a mi camino.”",
            "La Palabra de Dios puede ser una lámpara para tus pasos. Comparte cómo te sientes y buscaré una cita bíblica que te oriente.",
        )
