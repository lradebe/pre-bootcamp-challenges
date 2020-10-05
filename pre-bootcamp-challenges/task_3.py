#taking two user input numbers
a, b = input ("Guess first number: "), input ("Guess second number: ")
#convert both inputs into integers from string
a = int (a)
b = int (b)
#c is the sum of both inputs
c = a + b
#convert c into an integer
c = int (c)
#if either inputs are 65 or their sum is 65, print True
if a == 65 or b == 65 or c == 65:
    print ('TRUE!')
#if 65 doesn't show up in neither variables then it's False
else:
    print ('FALSE!')
print ("Thank you for playing!")
