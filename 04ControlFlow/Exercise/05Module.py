""" Name : 05Module.py
Author : Dan Thomas
Date : 08 Nov 2018
Purpose : Exercise working with control flow"""

import math


number = float(input("Please enter number to calculate the square root of: "))
if number < 1:
    print("Enter a positive number!")
else:
    print("Square root of",number,"is",math.sqrt(number))
