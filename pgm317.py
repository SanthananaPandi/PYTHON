# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 19:11:41 2024
Call the same function with four times with different data
@author: santh
"""

def num(*x):
    for i in x:
        print(i)
        
#main
num(1,2,3,4,5,6)
num(1.0,2.0,3.0,4.0)
num(1000,2000,3000,4000)
num(121,221,321,421)