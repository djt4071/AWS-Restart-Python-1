""" Name : 01FileWrite.py
Author : Dan Thomas
Date : 09 Nov 2018
Purpose : Example writing file """

file = open("filename.txt","w")
for n in range(1,11):
    newline = "This is line " + str(n) + "\n"
    file.write(newline)

file.close()
