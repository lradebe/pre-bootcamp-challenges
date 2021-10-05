def maximum(num1, num2, num3):

    if num1 >= num2 and num1 >=num3:
        highest = num1
    elif num2 >= num1 and num2 >= num3:
        highest = num2
    elif num3 >= num1 and num3 >= num2:
        highest = num3
    print(highest)
