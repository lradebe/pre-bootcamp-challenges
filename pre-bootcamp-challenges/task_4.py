def find_3(num1, num2):

  num3 = num1 + num2
  num3 = str(num3)

  if num1 == 3 and num3.find('3') == -1:
      print("FALSE")

  elif num2 == 3 and num3.find('3') == -1:
      print('FALSE')

  elif num1 == 3 and num3.find('3'):
      print("TRUE!")

  elif num2 == 3 and num3.find('3'):
      print('TRUE!')

  else:
      print("False")

find_3(5, 9)
