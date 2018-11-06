""" Name : 08BODMAS
Author : Dan Thomas
Date : 06 Nov 2018
Purpose : Example of simple maths """

number1 = float(input('Please enter your first number:  '))

answer = number1 * 3 + 4
print(number1,'* 3 + 4 =',answer)

answer = 3 + 4 * number1
print('3 + 4 *',number1,'=',answer)

answer = number1 * (3+4)
print(number1,'* (3 + 4) =',answer)
