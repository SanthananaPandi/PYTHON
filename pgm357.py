# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 11:38:16 2024
Count the number of vowels and non vowels in a given string
@author: santh
"""

def vowels(a):
    c=0
    b=0
    for i in a:
        if i in 'aeiou':
            b=b+1
        else:
            c=c+1
    return ("Vowels : ",b,"Non Vowels:",c)
#main
a=input("Enter the text : ")
x=vowels(a)
print(x)