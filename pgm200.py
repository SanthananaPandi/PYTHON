# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 16:19:00 2023
Copy all the characters from the Mth position
@author: santh
"""
s1=input("Enter the value of s1: ")
s2=''
n=len(s1)
m=int(input("Enter the value of m: "))
for i in range(m,n):
    s2=s2+s1[i]
print(s2)
