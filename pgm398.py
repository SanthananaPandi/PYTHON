# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 17:24:01 2024
Display the first five records of the excel file.
@author: santh
"""

import csv
f=open("students.csv")
x=csv.reader(f)
a=next(x)
b=next(x)
c=next(x)
d=next(x)
e=next(x)
print(a)
print(b)
print(c)
print(d)
print(e)
f.close()