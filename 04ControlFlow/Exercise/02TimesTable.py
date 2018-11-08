""" Name : 02TimesTable.py
Author : Dan Thomas
Date : 08 Nov 2018
Purpose : Exercise working with control flow"""


table = int(input("Enter a times table: "))

if table < 1:
        print("Enter a number above 0!")
elif table < 12:
    for i in range(13):
        print(i,"*",table,"=",i*table)
else:
    print("Enter a number less than 12!")


for i in range(13):
    for j in range(13):
        print(i,"*",j,"=",i*j)
