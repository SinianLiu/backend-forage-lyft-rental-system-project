import pytest
from datetime import date
from battery.spindler_battery import SpindlerBattery

class TestSpindlerBattery:

  @pytest.mark.parametrize(
    "date1,date2,expected_result",
    [
      (date.fromisoformat("2020-05-15"), date.fromisoformat("2018-01-25"), False),
      (date.fromisoformat("2020-05-15"), date.fromisoformat("2019-01-10"), False),
    ]
  )

  def test_spindler_battery(self, date1, date2, expected_result):
    battery = SpindlerBattery(date1, date2)
    assert battery.needs_service() == expected_result