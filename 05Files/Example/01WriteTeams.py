""" Name : 01WriteTeams.py
Author : Dan Thomas
Date : 09 Nov 2018
Purpose : Exercise writing file """

file = open("teams.txt","w")
teams = ["Manchester United","Arsenal","Manchester City","Liverpool","Salford"]
for t in teams:
    line = str(t) + " is a football team." + "\n"
    print(line)
    file.write(line)
file.close()

