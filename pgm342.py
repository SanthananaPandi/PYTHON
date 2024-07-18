# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 18:34:49 2024
Convert fahrenheit to temperature from 0 to 100 using map function
@author: santh
"""

def temperature(f):
    s=5/9 * (f-32)
    return s

#main
f=[ i for i in range(101)]
x=map(temperature,f)
print(list(x))
