""" Name : 05IfNested.py
Author : Dan Thomas
Date : 08 Nov 2018
Purpose : Exercise working with control flow"""

number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

print("Menu:")
print("1 - Plus")
print("2 - Minus")
print("3 - Multiply")
print("4 - Divide")

optionselected = int(input("Enter mathematical operation: "))

if optionselected == 1:
    answer = (number1 + number2)
    print(number1,"+",number2,"=",answer)

elif optionselected == 2:
    answer = (number1 - number2)
    print(number1,"-",number2,"=",answer)
    
elif optionselected == 3:
    answer = (number1 * number2)
    print(number1,"*",number2,"=",answer)
    
elif optionselected == 4:
    anser = (number1 / number2)
    print(number1,"/",number2,"=",answer)
    
else:
    print("Choose between 1 and 4 on the menu!")
