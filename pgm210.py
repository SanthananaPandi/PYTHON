# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 17:00:42 2023
Copy last n characters from the right edge
@author: santh
"""
s1=input("Enter the value of s1 :")
s2=''
m=int(input("Enter the value of m: "))
n=len(s1)
x=n-m
for i in range(x,n):
    s2=s2+s1[-i]
print(s2)

