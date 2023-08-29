# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 10:17:14 2023
Copy n character from the right edge mth position
@author: santh
"""
s1=input("Enter the value of s1: ")
n=int(input("Enter the value of n: "))
m=int(input("Enter the value of m: "))
s2=''
i=m
while i<=m+n:
    s2=s2+s1[-i]
    i=i+1
print(s2)

