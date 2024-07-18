# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 18:08:28 2024
Find the union,intersection and intersection of the given two sets
@author: santh
"""

import random as rd
a=[rd.randint(-100,100)for i in range(50)]
b=[rd.randint(-100,100)for i in range(50)]
c=set(a)
d=set(b)
x=c.union(d)
y=c.intersection(d)
z=c.difference(d)
print("Union : ",x)
print("Intersection : ",y)
print("Difference : : ",z)