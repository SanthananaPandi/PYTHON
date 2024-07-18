# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 16:51:22 2023
Given integer number is palindrome or not
@author: santh
"""
a=int(input("Enter the value of a: "))
s1=str(a)
s2=''
n=len(s1)
a=n-1
for i in range(a,-1,-1):
    s2=s2+s1[i]
b=int(s2)
if s1==s2:
    print("Palindrome")
else:
    print("Not")


