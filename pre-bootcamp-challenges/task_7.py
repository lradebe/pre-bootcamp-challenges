def get_F ():
  C_t = input ("What is the temperature in °C? ")
  C_t = int (C_t)
  sum = C_t * 9/5 + 32
  print ("°C in Fereignheit is: ", sum)
get_F ()

def get_C ():
  F_t = input ("What is the temperature in Fereignheit? ")
  F_t = int (F_t)
  sum = (F_t - 32)* 5/9
  print ("Fereignheit in °C is: ", sum)

get_C ()
