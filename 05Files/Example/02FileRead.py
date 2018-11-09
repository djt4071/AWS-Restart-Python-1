""" Name : 02FileRead.py
Author : Dan Thomas
Date : 09 Nov 2018
Purpose : Exercise writing file """

file = open("filename.txt","r")
print("First line:")
print(file.readline())
print("Second line:")
print(file.readline())
print("Rest of file:")
print(file.readline())
print("Blank line:")
print(file.readline(4))

file.close()
