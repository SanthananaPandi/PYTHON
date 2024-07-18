# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:29:10 2024
Print the value of a sin while pass into the functions
@author: santh
"""

import math
def math_sin(x, y):
    s = y(x)
    print(s)

# main    
x=int(input("Enter the value of x : "))
math_sin(x, math.sin)

