#defining a function that takes the temp in Celcius 
#and converts it to Fereignheit
def get_F ():

#taking input of Celcius temperature
  C_t = input ("What is the temperature in °C? ")
#converting input into an integer
  C_t = int (C_t)
#formula that actually does the conversion to fereignheit
  sum = C_t * 9/5 + 32
  print ("°C in Fereignheit is: ", sum)

#calling out function
get_F ()


#defining  function that does reverse of first function
def get_C ():

  F_t = input ("What is the temperature in Fereignheit? ")

  F_t = int (F_t)

  sum = (F_t - 32)* 5/9

  print ("Fereignheit in °C is: ", sum)

#calling out function
get_C ()
