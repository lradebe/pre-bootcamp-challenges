#taking two user input numbers
a, b = input ("Try your luck: "), input ("Try again: ")
#convert both inputs into integers
a = int (a)
b = int (b)
#c is a sum of both integers
c = a + b
#convert c into a string so we can use the find () function later
c = str (c)

#if a is 3 AND you DON'T find 3 in c then it's false
if a == 3 and c.find ('3') == -1:

    print ("FALSE")
#else if b is 3 AND you DON'T find 3 in c, print false again
elif b == 3 and c.find ('3') == -1:

    print ('False')

#else if a is 3 and you find 3 in c, it's true
elif a == 3 and c.find ('3'):

    print ("TRUE!")

#else if b is 3 and you find 3 in c, it's true
elif b == 3 and c.find ('3'):

    print ('TRUE!')
#if all previous statements aren't fit, then it's false
else:

    print ("False")
