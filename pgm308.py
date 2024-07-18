# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 22:59:46 2024
Area of circle using function
@author: santh
"""

def circle (r):
    s=22/7 * (r*r)
    return s

#main

r=int(input("Enter the value of r : "))
s=circle(r)
print(s)
