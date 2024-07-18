# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 16:46:52 2023
Reverse the string
@author: santh
"""
s1=input("Enter the value of s1 :")
s2=''
n=len(s1)
a=n-1
for i in range(a,-1,-1):
    s2=s2+s1[i]
print(s2)