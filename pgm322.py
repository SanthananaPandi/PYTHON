# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:02:05 2024
Pass bio data to the function and print it field by field.
@author: santh
"""

def bio(**x):
    for i in x:
        print(i,x[i])
        
#main
bio(Name='Vijay',age=23,Gender='Male',city='Trichy')