from django.test import TestCase
from testapp.models import Speedboat


class SpeedBoatTest(TestCase):
    """
    Test for Payment
    """
    def setUp(self):
        self.speedboat = Speedboat()

    def test_nothing(self):
        self.assertEqual(1, 1)
