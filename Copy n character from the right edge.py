# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 10:04:23 2023
Copy n character from the right edge
@author: santh
"""
s1=input("Enter a value of s1: ")
n=int(input("Enter the value of n: "))
s2=''
i=1
while i<=n:
    s2=s2+s1[-i]
    i=i+1
print(s2)|
