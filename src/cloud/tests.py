from django.test import TestCase
from cloud.management import commands


def AWSTestCase():
    def test_setup_cloud(self):
        self.assertEqual(commands.setupcloud(), None)
