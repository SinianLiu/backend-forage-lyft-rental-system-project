# pytest version

import pytest
from datetime import date
from battery.nubbin_battery import NubbinBattery

class TestNubbinBattery:

  @pytest.mark.parametrize(
    "date1,date2,expected_result",
    [
      (date.fromisoformat("2020-05-15"), date.fromisoformat("2016-01-25"), False),
      (date.fromisoformat("2020-05-15"), date.fromisoformat("2019-01-10"), False),
    ]
  )

  def test_nubbin_battery(self, date1, date2, expected_result):
    battery = NubbinBattery(date1, date2)
    assert battery.needs_service() == expected_result



# unittest version 
import unittest
from datetime import date
from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2016-01-25")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())