# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 18:00:30 2023
Given character is upper or not using the unicode
@author: santh
"""
n=input("Enter the value of n: ")
a=ord(n)
if a>=65 and a<=90:
    print(n,"is a upper case")
else:
    print(n,"is not an upper case")    
