# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 19:41:56 2023
Print the pattern   *****
                     ****
                      ***
                       **
                        *
                       **
                      ***
                     ****
                    ***** 
@author: santh
"""
n=5
for i in range(0,5):
    print(" " * i + "*" * n)
    n=n-1
m=2
for i in range(3,-1,-1):
    print(" " * i + "*" * m)
    m=m+1
