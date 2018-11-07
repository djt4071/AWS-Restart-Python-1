""" Name : 03Decimal.py
Author : Dan Thomas
Date : 07 Nov 2018
Purpose : Exercise importing a class """

from decimal import *
number1 = 1
number2 = 7

print(type(number1))
print(number1 / number2)

number1 = Decimal(1)
number2 = Decimal(7)
print(type(number1))
print(number1 / number2)
