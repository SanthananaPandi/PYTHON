# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 18:03:01 2023
Construct a list of even numbers from 100 to 300 using list comphrension
@author: santh
"""

a=[i for i in range(100,301) if i%2==0]
print(a)