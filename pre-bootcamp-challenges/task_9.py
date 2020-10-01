numbers = range (0, 1000)
multiples = 0

for i in numbers:
#if there is no remainder when diving 3/5 from i
  if i % 3 == 0 or i % 5 == 0:
#then add whatever value found in multiples with both values of i
    multiples += i
#when i has reached 1000, max multiples have been reached and added togeth>
print (multiples)
