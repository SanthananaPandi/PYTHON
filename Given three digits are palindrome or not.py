# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 19:22:56 2023
Given three digits are palindrome or not
@author: santh
"""
a=int(input("Enter the value of a "))
x=a%10
y=a//10
z=y%10
w=y//10
b=x*100
c=z*10
d=w*1
e=b+c+d
if a==e:
    print(a,"is a palindrome")
else:
    print(a,"is not a palindrome")    
