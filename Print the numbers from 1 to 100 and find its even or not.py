# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 22:26:56 2023
Print the numbers from 1 to 100 and find its even or not
@author: santh
"""
c=1
while c<=100:
    d=c%2
    if d==0:
        print("even")
    else:
        print("Not")
    print(c)
    c=c+1
