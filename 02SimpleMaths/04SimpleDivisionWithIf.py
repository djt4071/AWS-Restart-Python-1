""" Name : 04Division
Author : Dan Thomas
Date : 06 Nov 2018
Purpose : Example of simple maths """

number1 = float(input('Please enter your first number:  '))
number2 = float(input('Please enter your second number:  '))

if number2 == 0:
    print("You are attempting to divide by 0!")
else:
    answer = number1 / number2
    print(number1, ' / ', number2, ' = ', answer)
