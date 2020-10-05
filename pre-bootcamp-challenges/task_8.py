#defining a function that converts numbers into time format
def c_n ():
#to use time.delta which actually does the conversion
#we'll need to import datetime function
  import datetime

  a = input ("Punch number: ")
  a = int (a) #turn input into an integer

#print the conversion as a string
#use timedelta which is found in datetimd
#assign a to minutes in the format
#[:-3] tells python how many digits we want to see in our output
#[:-1] would show us more, [:-4] would show us less
  print (str (datetime.timedelta (minutes = a))[:-3])

#call out function
c_n ()
