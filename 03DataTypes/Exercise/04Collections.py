""" Name : 04Collections.py
Author : Dan Thomas
Date : 07 Nov 2018
Purpose : Exercise working with collections"""

fruits = list([0,1,2,3])
fruits[0] = input("Please enter a fruit:")
fruits[1] = input("Please enter another fruit:")
fruits[2] = input("And another fruit:")
fruits[3] = input("And another fruit, Carol:")

dictfruits = {1 : fruits[0],
              2 : fruits[1],
              3 : fruits[2],
              4 : fruits[3]}

print(fruits)
print(set(fruits))
print(dictfruits)

