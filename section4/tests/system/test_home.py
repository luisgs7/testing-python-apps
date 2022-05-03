from unittest import TestCase
import json

from section4.app import app


class TestHome(TestCase):
    def test_home(self):
        with app.test_client() as c:
            resp = c.get("/")

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(json.loads(resp.get_data()), {"message": "Hello World"})
