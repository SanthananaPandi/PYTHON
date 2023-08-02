# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 22:42:47 2023
Read the character other than $ and find it is a upper or lower or digits or special character.
@author: santh
"""
a=input("Enter the value of a: ")
while a!='$':
    if a >='A' and a <='Z' :
        print(L"is a uppercase")
    elif a >='a' and a <='z' :
        print("is a lowercase")
    elif a >= '0' and a<='9' :
        print("is a digit")
    else:
        print("is a special character")
    print(a)
    a=input("Enter the value of a:: ")    
