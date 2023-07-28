# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 22:29:36 2023
Smallest of three integer number
@author: santh
"""
a=int(input("Enter the value of a "))
b=int(input("Enter the value of b "))
c=int(input("Enter the value of c "))
if a<b:
    if a<c:
        print(a,"is smaller")
    else:
        print(c,"is smaller")
else:
    if b<c:
        print(b,"is smaller")    
    else:
         print(c,"is smaller")

