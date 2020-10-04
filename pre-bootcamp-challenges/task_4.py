a, b = input ("Try your luck: "), input ("Try again: ")
a = int (a)
b = int (b)
c = a + b
c = str (c)

if a == 3 and c.find ('3') == -1:

    print ("FALSE")

elif b == 3 and c.find ('3') == -1:

    print ('False')

else:
    print ("TRUE!")
