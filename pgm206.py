# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 16:53:30 2023
Reverse the string using negative indexing
@author: santh
"""
s1=input("Enter the value of s1 :")
s2=''
n=len(s1)
a=-n
for i in range(-1,a,-1):
    s2=s2+s1[i]
print(s2)
