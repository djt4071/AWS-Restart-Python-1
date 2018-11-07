""" Name : 03Boolean.py
Author : Dan Thomas
Date : 07 Nov 2018
Purpose : Exercise working with booleans """

print("This program orders animals alphabetically!")
animal1 = input("Input the first animal:")
animal2 = input("Input the second animal:")

if animal1 > animal2:
    print(animal2,animal1, sep= ' ')

else:
    print(animal1,animal2, sep= ' ')
