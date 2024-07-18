# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 19:59:39 2023
Print the pattern  *******
                    *****
                     ***
                      *
@author: santh
"""
for i in range(3,-1,-1):
    print(" " * (3-i),"*" * ((2*i)+1))
