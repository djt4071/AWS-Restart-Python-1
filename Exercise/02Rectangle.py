""" Name : 02Rectangle.py
Author : Dan Thomas
Date : 06 Nov 2018
Purpose : Example of calculating length and area """

length = float(input('Please enter rectangle length:  '))
width = float(input('Please enter rectangle width:  '))
height = float(input('Please enter rectangle height:  '))

if length > width:
    perimeter = (length * 2) + (width * 2)
    area = length * width
    volume = (length * width * height)
    print('Perimeter = ',perimeter,'m')
    print('Area = ',area,'m2')
    print('Volume = ',volume,'m3')

else:
    print('The Length should be greater than the width of a rectangle!')

