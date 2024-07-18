# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 19:50:52 2023
Print the pattern   *
                   ***
                  *****
                 ******* 
@author: santh
"""
x=1
for i in range(4,0,-1):
    print(" " * i + "*" * x)
    x=x+2
