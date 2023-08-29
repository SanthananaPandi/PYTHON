# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 18:30:46 2023
Copy N character from the M th position
@author: santh
"""
s1=input("Enter the value of s1: ")
n=int(input("Enter the value of n: "))
s2=''
m=int(input("Enter the value of m: "))
i=m
while i<=m+n:
    s2=s2+s1[i]
    i=i+1
print(s2)
