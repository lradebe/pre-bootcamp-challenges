def c_n ():
  import datetime

  a = input ("Punch number: ")
  a = int (a)
  print (str (datetime.timedelta (minutes = a))[:-3])

c_n ()
