""" Name : 07Modulo
Author : Dan Thomas
Date : 06 Nov 2018
Purpose : Example of simple maths """

number1 = float(input('Please enter your first number:  '))
number2 = float(input('Please enter your second number:  '))

if number2 == 0:
    print('Number 2 is 0!')
else:
    answer = number1 % number2
    print(number1, ' % ',number2,' = ',answer)
