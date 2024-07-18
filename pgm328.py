# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 19:16:13 2024
Calculate the area of a circle by passing a function to the function
@author: santh
"""

def circle(r):
    s=22/7 *(r*r)
    return s

def calculate (r,x):
    s=x(r)
    print(s)
    
#main
r=int(input("Enter the value of r : "))
calculate(r,circle)