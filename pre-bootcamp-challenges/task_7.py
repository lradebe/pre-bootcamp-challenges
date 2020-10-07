#defining a function that takes the temp in Celcius 
#and converts it to Fereignheit
def get_Fereignheit_temp():

#taking input of Celcius temperature
  celcius_temp = input("What is the temperature in °C? ")
#converting input into an integer
  celcius_temp = int(celcius_temp)
#formula that actually does the conversion to fereignheit
  sum = celcius_temp * 9/5 + 32
  print("°Celcius in Fereignheit is: ", sum)

#calling out function
get_Fereignheit_temp()


#defining  function that does reverse of first function
def get_celcius_temp():

  Fereignheit_temp = input("What is the temperature in Fereignheit? ")

  Fereignheit_temp = int(Fereignheit_temp)

  sum = (Fereignheit_temp - 32)* 5/9

  print("Fereignheit in °C is: ", sum)

#calling out function
get_celcius_temp()
