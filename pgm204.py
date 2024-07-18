# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 16:49:32 2023
Given string is palindrome or not
@author: santh
"""
s1=input("Enter the value of s1 :")
s2=''
n=len(s1)
a=n-1
for i in range(a,-1,-1):
    s2=s2+s1[i]
if s1==s2:
    print("Palindrome")
else:
    print("Not")
