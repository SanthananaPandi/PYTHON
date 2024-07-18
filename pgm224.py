# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 15:55:40 2023
Copy n characters from the mth position using negative indexing
@author: santh
"""
s=input("Enter the value of s: ")
n=int(input("Enter the value of n: "))
m=int(input("Enter the value of m: "))
x=m+n
s1=s[-m:-x:-1]
print(s1)