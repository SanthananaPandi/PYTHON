# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 18:07:43 2023
Given character is upper,lower,digit or special character using a unicode
@author: santh
"""
n=input("Enter the value of n: ")
a=ord(n)
if a>=65 and a<=90:
    print(n,"is a upper case")
elif a>=97 and a<=122:
    print(n,"is a lower case")
elif a>=48 and a<=57:
    print(n,"is a digit")
else:
    print(n,"is a special character")    
