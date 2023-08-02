# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 22:48:19 2023
Read the character other than $ and find its count of a upper,lower,digits and special character.
@author: santh
"""
a=input("Enter the value of a: ")
b=c=d=e=0
while a!='$':
    if a >='A' and a <='Z' :
        b=b+1
    elif a >='a' and a <='z' :
        c=c+1
    elif a >= '0' and a<='9' :
        d=d+1
    else:
        e=e+1
    a=input("Enter the value of a:: ") 
print(b)
print(c)
print(d)
print(e)
