# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 15:13:39 2024
construct a set of n random numbers using set comphrension
@author: santh
"""

import random as rd
n=int(input("Enter the value of n : "))
a={rd.randint(-100,100)for i in range(n)}
print(a)