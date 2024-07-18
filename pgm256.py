# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 19:10:30 2023
Construct a n list of random numbers and extract into a single,two,three and four digits into a list.
@author: santh
"""

import random as rd
x=[rd.randint(-1,10000) for i in range(100)]
a=[i for i in x if i>=0 and i<=9]
b=[i for i in x if i>=10 and i<=99]
c=[i for i in x if i>=100 and i<=999]
d=[i for i in x if i>1000 and i<=9999]
print(a)
print(b)
print(c)
print(d)