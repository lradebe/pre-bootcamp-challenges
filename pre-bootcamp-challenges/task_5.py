#return area of triangle using sides

#taking 3 user inputs and turning them into floats
a = float (input ('Enter first side: '))
b = float (input ('Enter second side: '))
c = float (input ("Enter base side: "))

#we're about to do some math so i have to import math functions
import math

#Calculating s, the triangle's semi-parameter
s = (a + b + c)/2
#Calculating the triangle's area
Area = math.sqrt (s*(s-a)*(s-b)*(s-c))

#converting the calculated value of the Area into a string
#so it can be used in a sentence later.
Area = str (Area)

print ("The area of the triangle is: " + Area)
