# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 15:24:51 2023
Copy the last N character(N)
@author: santh
"""
s=input("enter the value of s: ")
n=len(s)
m=int(input("Enter the value of m: "))
a=n-m
s1=s[a:n]
print(s1)