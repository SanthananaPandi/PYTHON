# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 19:12:53 2023
Print Upper to Lower
@author: santh
"""
u=input("Enter the value of u: ")
a=ord(u)
if a>=65 and a<=90:
    b=a+32
    c=chr(b)
    print(u,"lower case is",c)
else:
    print("Not")    
