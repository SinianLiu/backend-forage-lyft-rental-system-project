from battery.battery import Battery
from utils import add_years_to_date

class SpindlerBattery(Battery):
  def __init__(self, current_date, last_date):
    self.current_date = current_date
    self.last_date = last_date

  def needs_service(self):
    planned_next_service_date = add_years_to_date(self.last_date, 4)
    if planned_next_service_date < self.current_date:
      return True
    else:
      return False
