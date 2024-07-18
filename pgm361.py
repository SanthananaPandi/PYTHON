# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:57:21 2024
Count the number of Vowels and Non-vowels using global variable.
@author: santh
"""

b=c=0
def vowels(a):
    global b,c
    for i in a:
        if i in 'aeiou':
            b=b+1
        else:
            c=c+1
#main
a=input("Enter the value of a : ")
vowels(a)
print("Vowels :",b)
print("Non Vowels :",c)
            