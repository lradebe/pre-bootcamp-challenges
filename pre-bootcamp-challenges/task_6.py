#Create a function that takes three numbers and 
#returns the highest

#defining my first function, it gets the maximum
#number from any string
def highest (n):
#assigning 0 into i
  i = 0
  highest = n [i]

#for i in the range from 1 to where ever the string of n ends
  for i in range (1, len (n)):

#if our highest number is smaller than whatever value is in i 
#as it increments
    if (highest < n [i]):

#assign that value into highest
      highest = n [i]
#then tell what is the highest value
  print ("The highest value is " ,highest)

#defining a function that takes three numbers
def user ():

#take input from user and turn all values into integers
  d, c, b = input ("Put Number: "), input ("Put Number: "), input ("Put number: ")

  d = int (d)
  c = int (c)
  b = int (b)
#x is a collection of all input in one place, not a sum
  x = b, c, d
#call out the earlier created function that prints the highest number
#found in our collection variable, x.
  x = highest (x)

#use the function that does the ultimate job
#meaning it uses the first function within it too

user()
