# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 22:35:34 2023
Given string is palindrome or not
@author: santh
"""
s1=input("Enter the value of s1:")
s2=''
n=len(s1)
a=n-1
i=a
while i>=0:
    s2=s2+s1[i]
    i=i-1
if s1==s2:
        print("It is a palindrome")
else:
       print("Not")
    
