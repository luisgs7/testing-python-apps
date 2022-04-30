from unittest import TestCase
from section3.post import Post


class PostTest(TestCase):
    def test_create_post(self):
        p = Post("Test", "Test Content")

        self.assertEqual(p.title, "Test")
        self.assertEqual(p.content, "Test Content")

    def test_json(self):
        p = Post("Test", "Test Content")
        expected = {"Title": "Test", "Content": "Test Content"}

        self.assertDictEqual(p.json(), expected)
