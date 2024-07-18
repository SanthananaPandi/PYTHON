# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 18:33:49 2023
Construct a list of random numbers using list comphrension
@author: santh
"""

import random as rd
a=[rd.randint(-100,100) for i in range(100)]
print(a)