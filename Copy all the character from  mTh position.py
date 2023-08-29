# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 19:34:54 2023
Copy all the character from  mTh position
@author: santh
"""
s1=input("Enter the value of s1: ")
n=len(s1)
s2=''
m=int(input("Enter the value of m: "))
i=m
while i<=n-1:
    s2=s2+s1[i]
    i=i+1
print(s2)
