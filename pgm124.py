# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 19:31:58 2023
Extract n characters
@author: santh
"""
s1=input("Enter the value of s1 :")
n=int(input("Enter the value of n :"))
s2=''
i=0
while i<=n-1:
    s2=s2+s1[i]
    i=i+1
print(s2)
