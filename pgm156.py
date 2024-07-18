# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 19:50:35 2023
Print the years from 1000 to 3000 and find it is leap year or not
@author: santh
"""
for i in range(1000,3001):
    d=i%4
    if d==0:
        print(i," is a leap year")
    else:
        print(i," is not a leap year")
