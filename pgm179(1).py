# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 19:54:42 2023
Print the pattern   *
                   ***
                  *****
                 ******* 
@author: santh
"""
for i in range(0,4,1):
    print(" " * (3-i),"*" * ((2*i)+1))
