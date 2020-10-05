#defining a function that takes two words from user
#and must return common letters between them
def common ():

  wrd1, wrd2 = input ("First word: "), input ('Second word: ')

#convert both inputs into sets
  w1 = set (wrd1)
  w2 = set (wrd2)

#once they're sets use & to take common letters
#between both sets
#turn whatever common letters found into a list
  lst = list (w1 & w2)

#print common letters in a list format
  print ('Common letters: {}'.format (lst))

#call out function
common ()
