# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 18:03:38 2023
Given character is lower or not using the unicode
@author: santh
"""
n=input("Enter the value of n: ")
a=ord(n)
if a>=97 and a<=122:
    print(n,"is a lower case")
else:
    print(n,"is not an lower case") 
