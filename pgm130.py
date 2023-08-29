# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 10:07:50 2023
Given integer is palindrome or not
@author: santh
"""
a=int(input("Enter a value of a: "))
s1=str(a)
n=len(s1)
s2=''
x=n-1
i=x
while i>=0:
    s2=s2+s1[i]
    i=i-1
b=int(s2)
if s2==s1:
    print("palindrome")
else: 
    print("Not a palindrome")



        
