# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 15:37:14 2023
Given string is palindrome or not
@author: santh
"""
a=input("Enter the value of a: ")
b=a[::-1]

if a==b:
    print("Palindrome")
else:
    print("Not")