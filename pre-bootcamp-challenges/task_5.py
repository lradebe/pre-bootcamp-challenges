def triangle_area(num1, num2, num3):
  import math
  s = (num1 + num2 + num3)/2
  body = (s * (s-num1) * (s-num2) * (s-num3))
  Area = math.sqrt(body)
  print(f"The area of the triangle is: {Area}")
