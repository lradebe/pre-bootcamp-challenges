def convert_number_to_time(number):
  import datetime
  print(str(datetime.timedelta (minutes = number))[:-3])
