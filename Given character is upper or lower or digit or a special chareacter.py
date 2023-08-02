# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 09:30:29 2023
Given character is upper or lower or digit or a special chareacter
@author: santh
"""
n=input("Enter the value of n: ")
if n >='A' and n <='Z' :
    print(n,"is a uppercase")
elif n >='a' and n <='z' :
    print(n,"is a lowercase")
elif n >= '0' and n<='9' :
    print(n,"is a digit")
else:
    print(n,"is a special character")
