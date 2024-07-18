# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 16:55:36 2023
Reverse the string using negative indexing (Use absolute value)
@author: santh
"""
s1=input("Enter the value of s1 :")
s2=''
n=len(s1)
for i in range(1,n):
    s2=s2+s1[-i]
print(s2)
