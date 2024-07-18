# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 18:54:23 2024
Construct a list of n random numbers using lambda using function
@author: santh
"""

import random as rd
x=lambda n :[rd.randint(-1000,1000)for i in range(n)]
n=int(input("Enter the value of n : "))
y=x(n)
print(y)