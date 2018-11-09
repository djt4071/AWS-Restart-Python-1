""" Name : 03FileReadByLine.py
Author : Dan Thomas
Date : 09 Nov 2018
Purpose : Exercise writing file """

file = open("filename.txt","r")
print("First line:")
print(file.readline())
file.seek(0)
print("First line again:")
print(file.readline())

file.close()
