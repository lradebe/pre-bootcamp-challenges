a, b = input ("Guess first number: "), input ("Guess second number: ")
a = int (a)
b = int (b)
c = a + b

if a == 65 or b == 65 or c == 65:
    print ('TRUE!')
else:
    print ('FALSE!')
print ("Thank you for playing!")
