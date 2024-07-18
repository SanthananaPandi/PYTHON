# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 16:35:09 2023
Copy N characters from the M th position
@author: santh
"""
s1=input("Enter the value of s1: ")
s2=''
m=int(input("Enter the value of m: "))
n=int(input("Enter the value of n: "))
x=m+n
for i in range(m,x):
    s2=s2+s1[i]
print(s2)