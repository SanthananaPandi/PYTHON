# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 20:02:32 2024
Construct a tuple of n random numbers and print it
@author: santh
"""

import random as rd
n=int(input("Enter the value of n: "))
x=[rd.randint(-100,100)for i in range(n)]
a=tuple(x)
print(a)