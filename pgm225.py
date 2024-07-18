# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 15:59:51 2023
Copy last n character of the right edge
@author: santh
"""
s=input("Enter the value of s: ")
n=len(s)
m=int(input("Enter the value of m: "))
x=m-n
s1=s[-x::-1]
print(s1)
