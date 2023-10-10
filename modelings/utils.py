
from datetime import datetime

def weekFromDate(date_string):
  '''
  Returns ISO week number based on a date string formatted as "yyyy-mm-dd"
  '''
  date = datetime.strptime(date_string, "%Y-%m-%d")
  week_number = date.isocalendar()[1]
  return week_number