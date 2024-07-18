# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 18:42:23 2024
Construct a 3x3 matrix using list comprehension
@author: santh
"""

import random as rd
a=[[rd.randint(-100,100)for i in range(3)]for j in range(3)]
print(a)