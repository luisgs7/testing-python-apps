from unittest import TestCase
from section3.blog import Blog


class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        b = Blog("Test", "Test author")
        b.create_post("Test Post", "Test Content")

        self.assertEqual(b.posts[0].title, "Test Post")
        self.assertEqual(b.posts[0].content, "Test Content")

    def test_json_no_posts(self):
        b = Blog("Test", "Test Author")
        expected = {"title": "Test", "author": "Test Author", "posts": []}

        self.assertDictEqual(expected, b.json())

    def test_json_with_posts(self):
        b = Blog("Test", "Test author")
        b.create_post("Test Post", "Test Content")

        self.assertDictEqual(
            b.json(),
            {
                "title": b.title,
                "author": b.author,
                "posts": [{"title": "Test Post", "content": "Test Content"}],
            },
        )
