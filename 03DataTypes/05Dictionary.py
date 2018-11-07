""" Name : 05Dictionary.py
Author : Dan Thomas
Date : 07 Nov 2018
Purpose : Exercise working with dictionary """

team = {"Clive" : 100}

team["Jack"] = 23
team["James"] = 17
team["Joe"] = 19
team["John"] = 20
print(team)
print(team["John"])
team["John"] = 33

print(team)

if "John" in team:
    print("This is the value requested:",team["John"])

else:
    print("Not in team dictionary!")
