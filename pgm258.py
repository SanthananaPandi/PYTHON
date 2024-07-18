# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 19:16:32 2023
Construct a set of two n random list and find the sum and differences of the
two list using list comprenhsion
@author: santh
"""

import random as rd
n=int(input("Enter the value of n : "))
x=[rd.randint(-1000,1000) for i in range(n)]
y=[rd.randint(-1000,1000) for i in range(n)]
a=[x[i] + y[i] for i in range(n)]
b=[x[i] - y[i] for i in range(n)]
print(a)
print(b)