# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 19:16:54 2023
Print lower to upper
@author: santh
"""
u=input("Enter the value of u: ")
a=ord(u)
if a>=97 and a<=122:
    b=a-32
    c=chr(b)
    print(u,"Upper case is",c)
else:
    print("Not")    

