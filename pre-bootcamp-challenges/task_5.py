#return area of triangle using sides
a = float (input ('Enter first side: '))
b = float (input ('Enter second side: '))
c = float (input ("Enter base side: "))
import math
#s is semi-parameter
s = (a + b + c)/2
Area = math.sqrt (s*(s-a)*(s-b)*(s-c))
Area = str (Area)
print ("The area of the triangle is: " + Area)
