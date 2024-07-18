# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 18:10:33 2023
Construct a list of leap years from 1000 to 3000 using list comprhension 
@author: santh
"""

a=[i for i in range(1000,3001) if i%4==0]
print(a)