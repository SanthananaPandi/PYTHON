# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 18:06:58 2024
construct a set of n random numbers
@author: santh
"""

import random as rd
a=[rd.randint(-100,100)for i in range(50)]
s=set(a)
print(s)