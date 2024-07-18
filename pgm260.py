# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 19:12:59 2024
Construct a two matrices using list comphrension
@author: santh
"""

import random as rd
a=[[rd.randint(-100,100)for i in range(3)]for j in range(3)]
b=[[rd.randint(-100,100)for i in range(3)]for j in range(3)]
print(a)
print(b)