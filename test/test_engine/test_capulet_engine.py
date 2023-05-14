# pytest
import pytest
from engine.capulet_engine import CapuletEngine

class TestCapuletEngine:

  @pytest.mark.parametrize(
    "current_mileage, last_service_mileage, expected_result",
    [
      (30001, 0, True),
      (30000, 0, False),
    ]
  )

  def test_capulet_engine(self, current_mileage, last_service_mileage, expected_result):
    engine = CapuletEngine(current_mileage, last_service_mileage)
    assert engine.needs_service() == expected_result



# unittest
# import unittest
# from engine.capulet_engine import CapuletEngine


# class TestCapuletEngine(unittest.TestCase):
#     def test_needs_service_true(self):
#         current_mileage = 30001
#         last_service_mileage = 0
#         engine = CapuletEngine(current_mileage, last_service_mileage)
#         self.assertTrue(engine.needs_service())

#     def test_needs_service_false(self):
#         current_mileage = 30000
#         last_service_mileage = 0
#         engine = CapuletEngine(current_mileage, last_service_mileage)
#         self.assertFalse(engine.needs_service())