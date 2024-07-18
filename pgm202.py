# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 16:37:38 2023
Copy the last n character
@author: santh
"""
s1=input("Enter the value of s1: ")
s2=''
n=len(s1)
m=int(input("Enter the value of m: "))
a=n-m
for i in range(a,n):
    s2=s2+s1[i]
print(s2)
