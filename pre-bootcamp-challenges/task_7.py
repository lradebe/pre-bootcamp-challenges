def get_Fereignheit_temp(celcius_temp):

  fereignheit = celcius_temp * 9/5 + 32
  print("°Celcius in Fereignheit is:\t", fereignheit)

get_Fereignheit_temp(23)

def get_celcius_temp(Fereignheit_temp):

  celcius = (Fereignheit_temp - 32)* 5/9
  print("Fereignheit in °C is:\t", celcius)

get_celcius_temp(73)
