# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 19:52:33 2023
Print the pattern  *******
                    *****
                     ***
                      *
@author: santh
"""
x=7
for i in range (0,4):
    print(" " * i + "*" * x)
    x=x-2
