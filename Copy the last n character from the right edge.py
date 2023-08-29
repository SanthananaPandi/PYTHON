# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 10:17:14 2023
Copy the last n character from the right edge
@author: santh
"""
s1=input("Enter the value of s1: ")
n=len(s1)
m=int(input("Enter the value of m: "))
s2=''
a=n-m
i=a
while i<n+1:
    s2=s2+s1[-i]
    i=i+1
print(s2)
