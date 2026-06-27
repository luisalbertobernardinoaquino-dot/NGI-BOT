import unittest

from app import app


class AppTests(unittest.TestCase):
    def setUp(self):
        app.config.update(TESTING=True)
        self.client = app.test_client()

    def test_index_loads(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"NGI-BOT", response.data)
        self.assertIn(b"/static/css/style.css", response.data)
        self.assertIn(b"/static/js/app.js", response.data)

    def test_post_renders_question_and_response(self):
        response = self.client.post("/", data={"pregunta": "Tengo miedo"})

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Tengo miedo", response.data)
        self.assertIn("Isaías 41:10".encode(), response.data)

    def test_user_input_is_escaped(self):
        response = self.client.post(
            "/",
            data={"pregunta": "<script>alert(1)</script>"},
        )

        self.assertNotIn(b"<script>alert(1)</script>", response.data)
        self.assertIn(b"&lt;script&gt;alert(1)&lt;/script&gt;", response.data)

    def test_existing_images_are_served(self):
        for image_name in ("logo.png", "fondo.png", "ES.png"):
            with self.subTest(image=image_name):
                response = self.client.get(f"/static/images/{image_name}")
                self.addCleanup(response.close)
                self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
