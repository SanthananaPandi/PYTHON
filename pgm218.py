# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 15:32:14 2023
Copy the last N character
@author: santh
"""
s=input("enter the value of s: ")
n=len(s)
m=int(input("Enter the value of m: "))
a=n-m
s1=s[a:]
print(s1)
