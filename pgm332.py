# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:27:03 2024
Area of the circle using function within the function.
@author: santh
"""

def calculate():
    def circle(r):
        s=22/7 *(r*r)
        return s
    r=int(input("Enter the value of r : "))
    s=circle(r)
    print(s)
#main
calculate()
    
        