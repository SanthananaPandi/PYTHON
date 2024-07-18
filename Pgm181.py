# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 19:12:29 2023
Print the pattern        *
                        ***
                       *****
                      *******
                       *****
                        ***
                         *
@author: santh
"""
for i in range(0,4):
    print(" " * (3-i) + "*" * ((2*i)+1))
for i in range(2,-1,-1):
    print(" " * (2-i),"*" * ((2*i)+1))