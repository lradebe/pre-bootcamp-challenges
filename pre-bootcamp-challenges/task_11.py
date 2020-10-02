def common ():

  wrd1, wrd2 = input ("First word: "), input ('Second word: ')
  w1 = set (wrd1)
  w2 = set (wrd2)
  lst = list (w1 & w2)

  print ('Common letters: {}'.format (lst))

common ()
