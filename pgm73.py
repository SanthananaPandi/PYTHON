# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 22:36:01 2023
Print the year from 1000 to 3000 and find its leap year or not
@author: santh
"""
c = 1000
while c <= 3000:
    d = c % 4
    if d == 0:
        print("leap year")
    else:
        print("Not")
    print(c)
    c = c + 1

