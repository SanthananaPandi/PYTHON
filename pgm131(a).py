# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 10:00:54 2023
Use an absolute value
@author: santh
"""
s1=input("Enter a value of s1: ")
n=len(s1)
s2=''
i=1
while i<=n:
    s2=s2+s1[-i]
    i=i+1
print(s2)