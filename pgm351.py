# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 18:56:28 2024
Sum of the element of the list using lambda function.
@author: santh
"""

import random as rd
x=lambda n :[rd.randint(-1000,1000)for i in range(n)]
n=int(input("Enter the value of n : "))
element_1=x(n)
element_2=x(n)
sum=lambda n :[element_1[i] + element_2[i] for i in range(n)]
result=sum(n)
print(element_1)
print(element_2)
print(result)