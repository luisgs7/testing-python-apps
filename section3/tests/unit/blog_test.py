from unittest import TestCase
from section3.blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog("Test", "Test Author")

        self.assertEqual("Test", b.title)
        self.assertEqual("Test Author", b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test Author')
        c = Blog('My Day', 'Rolf')

        self.assertEqual(b.__repr__(), 'Test by Test Author (0 posts)')
        self.assertEqual(c.__repr__(), 'My Day by Rolf (0 posts)')
    
    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Test Author')
        b.posts = ['test']
        c = Blog('My Day', 'Rolf')
        c.posts = ['test', 'another']

        self.assertEqual(b.__repr__(), 'Test by Test Author (1 post)')
        self.assertEqual(c.__repr__(), 'My Day by Rolf (2 posts)')