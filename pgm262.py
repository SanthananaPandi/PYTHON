# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 19:21:01 2024
Differences of two matrices using list comphrension
@author: santh
"""

import random as rd
n=int(input("Enter the value of n : "))
a=[[rd.randint(-100,100)for i in range(3)]for j in range(3)]
b=[[rd.randint(-100,100)for i in range(3)]for j in range(3)]
x=[[a[i][j] - b[i][j]for i in range(n)]for j in range(n)]
print(x)