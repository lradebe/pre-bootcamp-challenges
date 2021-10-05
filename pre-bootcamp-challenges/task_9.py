numbers = range(0, 1000)
#we start with no multiples
multiples = 0


for i in numbers:
#if there is no remainder when diving 3 or 5 from i
  if i % 3 == 0 or i % 5 == 0:
#then add whatever value found in multiples with both values of i
    multiples += i
#when i has reached 1000
#max multiples have been reached and added together


#show the sum of all the multiples of 3 and 5 below 1000
print(multiples)
