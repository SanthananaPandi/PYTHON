# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 19:00:34 2024
Difference of the two elements of the list using lambda function.
@author: santh
"""

import random as rd
x=lambda n :[rd.randint(-1000,1000)for i in range(n)]
n=int(input("Enter the value of n : "))
element_1=x(n)
element_2=x(n)
Diff=lambda n :[element_1[i] - element_2[i] for i in range(n)]
result=Diff(n)
print(element_1)
print(element_2)
print(result)