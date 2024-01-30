from django.test import SimpleTestCase

from utils.env import EnvFile


class ParseEnvTestCase(SimpleTestCase):
    def setUp(self):
        self.env_file = EnvFile(".env.example")

    def test_parse_as_list(self):
        self.assertIsInstance(self.env_file.as_list(), list)

    def test_parse_as_string(self):
        self.assertIsInstance(self.env_file.as_string(), str)
