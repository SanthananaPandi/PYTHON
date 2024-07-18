# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 15:39:20 2023
Given integer number is palindrome or not
@author: santh
"""
a=int(input("Enter the value of a: "))
s=str(a)
b=s[::-1]

c=int(b)
if a==c:
    print("Palindrome")
else:
    print("Not")
