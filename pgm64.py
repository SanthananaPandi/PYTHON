# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 18:05:34 2023
Given character is digit or not using unicode
@author: santh
"""
n=input("Enter the value of n: ")
a=ord(n)
if a>=48 and a<=57:
    print(n,"is a digit")
else:
    print(n,"is not an digit") 
