import unittest

from chatbot import responder


class ChatbotTests(unittest.TestCase):
    def test_current_keyword_responses(self):
        cases = {
            "Me siento triste": "Salmo 34:18",
            "Tengo miedo": "Isaías 41:10",
            "Siento temor": "Isaías 41:10",
            "Tengo ansiedad": "Filipenses 4:6-7",
            "Estoy preocupado": "Filipenses 4:6-7",
            "Me siento solo": "Deuteronomio 31:8",
            "Siento soledad": "Deuteronomio 31:8",
            "Muchas gracias": "1 Tesalonicenses 5:18",
            "Estoy agradecido": "1 Tesalonicenses 5:18",
        }

        for pregunta, referencia in cases.items():
            with self.subTest(pregunta=pregunta):
                self.assertIn(referencia, responder(pregunta))

    def test_matching_is_case_insensitive(self):
        self.assertIn("Salmo 34:18", responder("ESTOY TRISTE"))

    def test_default_response(self):
        self.assertIn("Salmo 119:105", responder("Necesito orientación"))

    def test_rule_order_is_preserved(self):
        self.assertIn("Salmo 34:18", responder("Estoy triste y tengo miedo"))


if __name__ == "__main__":
    unittest.main()
