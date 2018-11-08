""" Name : 04Collections.py
Author : Dan Thomas
Date : 07 Nov 2018
Purpose : Exercise working with collections"""

fruits = []
fruitquantity = input("How many fruits do you have?")
                 
for quantity in fruitquantity:
    fruits.append(input("Please enter a fruit:"))

dictfruits = {}
count = 0
for fruit in fruits:
    dictfruits[fruits[count]] = count
    count +=1

print(fruits)
print(set(fruits))
print(dictfruits)

