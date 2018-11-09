""" Name : 05FileEdit.py
Author : Dan Thomas
Date : 09 Nov 2018
Purpose : Exercise writing file """

file = open("filename.txt","r")
outfile = ""
for line in range(10):
    if line % 2 == 0:
        outfile = outfile + file.readline()
    else:
        file.readline()

file = open("filename.txt", "w")
print(outfile)
file.write(outfile)
file.close()
