# pytest version
import pytest
from tires.carrigan_tires import CarriganTires


class TestCarriganTires:

  @pytest.mark.parametrize(
    "input,expected_result",
    [
      ([0.1, 0.3, 0.2, 0.9], True),
      ([0.1, 0.2, 0.4, 0.2], False),
    ]
  )

  def test_carrigan_tires(self, input, expected_result):
    tires = CarriganTires(input)
    assert tires.needs_service() == expected_result



# unittest version
import unittest
from tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
  def test_needs_service_true(self):
      tire_wear = [0.1, 0.3, 0.2, 0.9]
      tires = CarriganTires(tire_wear)
      self.assertTrue(tires.needs_service())

  def test_needs_service_false(self):
      tire_wear = [0.1, 0.2, 0.4, 0.2]
      tires = CarriganTires(tire_wear)
      self.assertFalse(tires.needs_service())