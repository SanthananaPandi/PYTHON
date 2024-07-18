# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 19:08:55 2024
Pass different number of arguments to the function and print it one by one
@author: santh
"""

def num(*z):
    for i in z:
        print(i)
        
#main
num(1,2,3,4,5,6,7)