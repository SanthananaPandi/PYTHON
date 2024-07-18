# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 22:58:38 2023
Extract a character other than vowels
@author: santh
"""
s=input("Enter the value of s: ")
z=''
for i in s:
    if i not in 'aeiou':
        z=z+i
print(z)
