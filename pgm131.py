# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 09:51:12 2023
Reverse the string using negative indexing
@author: santh
"""
s1=input("Enter a value of s1: ")
n=len(s1)
s2=''
a=-n
i=-1
while i>=a:
    s2=s2+s1[i]
    i=i-1
print(s2)



