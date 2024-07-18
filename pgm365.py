# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 10:34:22 2024
Read the function until you get 10 from the function
@author: santh
"""

def get():
    n=int(input("Enter the value of n : "))
    return n
#main
x=get()
while x!=10:
    print(x)
    x=get()
    