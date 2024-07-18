# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 18:14:53 2024
Square the number of list using map function
@author: santh
"""

def square(a):
    s=a*a
    return s
#main
n=int(input("Enter the value of n : "))
a=[int(input("Enter the value of a : "))for i in range (n)]
x=map(square,a)
print(list(x))
