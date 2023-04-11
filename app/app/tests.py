"""
Sample tests
"""

from django.test import SimpleTestCase

from . import calc

class CalcTests(SimpleTestCase):
  """test the calc module"""

  def test_add_numbers(self):
    """Test adding numbers together"""
    res = calc.add(5, 6)

    self.assertEqual(res, 11)

  def test_subtract_number(self):
    """test subract numbers"""
    res = calc.subract(10, 15)

    self.assertEqual(res, 5)