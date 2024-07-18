# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 18:40:23 2024
Construct a 3x3 matrix and print it using tuple
@author: santh
"""

import random as rd
a=[[rd.randint(-100,100)for i in range(3)]for j in range(3)]
x=tuple(a)
print(x)