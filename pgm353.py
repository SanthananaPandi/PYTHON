# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 19:02:06 2024
Construct a 3x3 matrix using lambda function
@author: santh
"""

import random as rd
matrix=lambda n :[[rd.randint(-100,100)for i in range(n)]for j in range(n)]
n=int(input("Enter the value of n : "))
y=matrix(n)
print(y)