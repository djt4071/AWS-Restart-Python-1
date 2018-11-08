""" Name : 07ForString.py
Author : Dan Thomas
Date : 08 Nov 2018
Purpose : Exercise working with control flow"""


vowels = ["a","e","i","o","u","A","E","I","O","U"]
word = input("Enter a word to count vowels and consonants: ")

vcount = 0
ccount = 0
for char in word:
    if char in vowels:
        vcount = vcount + 1
    else:
        ccount = ccount + 1
print("This word has",vcount,"vowels, and",ccount,"consonants.")

    
