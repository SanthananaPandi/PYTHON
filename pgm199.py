# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 16:16:40 2023
Extract n characters
@author: santh
"""
s1=input("Enter the value of s1: ")
s2=''
n=int(input("Enter the value of n: "))
for i in range(0,n):
    s2=s2+s1[i]
print(s2)
