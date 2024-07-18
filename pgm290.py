# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 15:16:31 2024
Construct a list of n random numbers and convert to set
@author: santh
"""

import random as rd
n=int(input("Enter the value of n : "))
a=[rd.randint(-100,100)for i in range(n)]
x=set(a)
print(x)