""" Name : 02Number.py
Author : Dan Thomas
Date : 07 Nov 2018
Purpose : Exercise converting number types """

from decimal import *

number1 = int(31)
number2 = int(19)


float1 = float(number1)
float2 = float(number2)

decimal1 = Decimal(number1)
decimal2 = Decimal(number2)

intanswer = int(number1 / number2)
floatanswer = float1 / float2
decanswer = decimal1 / decimal2

print(type(intanswer))
print(intanswer)

print(type(floatanswer))
print(floatanswer)

print(type(decanswer))
print(decanswer)
