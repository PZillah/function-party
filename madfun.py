#madfun.py

import math

num = eval(input("please enter a number: ")) #user inputs a decimal

#print absolute value of the number
print("the absolute value is", abs(num))
#print The number rounded to 0 decimal places
print("the number rounded is", round(num, 0))
#print The square root of the rounded number’s absolute value
print("the square root of the rounded number's absolute value is", math.sqrt(abs(round(num, 0))))
