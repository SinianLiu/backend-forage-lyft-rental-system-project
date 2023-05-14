# pytest version
import pytest
from tires.octoprime_tires import OctoprimeTires


class TestOctoprimeTires:

  @pytest.mark.parametrize(
    "input,expected_result",
    [
      ([0.8, 0.8, 0.8, 0.7], True),
      ([0.1, 0.2, 0.4, 0.2], False),
    ]
  )

  def test_carrigan_tires(self, input, expected_result):
    tires = CarriganTires(input)
    assert tires.needs_service() == expected_result