# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 22:24:52 2023
Biggest of three integer numbers
@author: santh
"""
a=int(input("Enter the value of a "))
b=int(input("Enter the value of b "))
c=int(input("Enter the value of c "))
if a>b:
    if a>c:
        print(a,"is greater")
    else:
        print(c,"is greater")
else:
    if b>c:
        print(b,"is greater")    
    else:
         print(c,"is greater")
