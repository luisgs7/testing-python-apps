from unittest import TestCase
from section4.app import app


class BaseTest(TestCase):
    def setUp(self) -> None:
        app.testing = True
        self.app = app.test_client
