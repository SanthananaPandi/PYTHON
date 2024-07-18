# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 22:29:39 2023
Read the string and count the string other than vowels
@author: santh
"""
a=input("Enter the value of a: ")
b=0
for i in a:
    if i not in 'aeiou':
        b=b+1
print(b)
