# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 17:40:24 2024
Display the each row of the excel sheet one by one.
@author: santh
"""

import csv
f=open("students.csv")
x=csv.reader(f)
a=next(x)
print(a)
for i in x:
    print(i)