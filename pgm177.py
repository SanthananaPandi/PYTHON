# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 19:36:57 2023
Print the pattern    *
                    **
                   ***
                  ****
                 *****
                  ****
                   ***
                    **
                     *
@author: santh
"""
k=1
for i in range (4,0,-1):
    print(" " * i + "*" * k)
    k=k+1
n=5
for i in range(0,5):
    print(" " * i + "*" * n)
    n=n-1