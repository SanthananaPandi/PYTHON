# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 18:54:26 2023
Construct a set of n random numbers and make addition,subraction,multiplication 
with a particular value on it and generate into a list...
@author: santh
"""

import random as rd
x=[rd.randint(1,100) for i in range(15)]
a=[i + 5 for i in x]
b=[i - 5 for i in x]
c=[i * 5 for i in x]
print(x)
print(a)
print(b)
print(c)