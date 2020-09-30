
def highest (n):
  i = 0
  highest = n [i]
  for i in range (1, len (n)):
    if (highest < n [i]):
      highest = n [i]
  print ("The highest value is " ,highest)

def user ():

  d, c, b = input ("Put Number: "), input ("Put Number: "), input ("Put number: ")
  d = int (d)
  c = int (c)
  b = int (b)
  x = b, c, d
  x = highest (x)

#def user_():

 # user = input ("Numbers: ")
  #if user == str (user):
   # user = int (user)
    #while user == int (user):
     # user =  input ("Numbers: ")
      #user = input ("Numbers: ")

#  user = highest (user)

user()
