# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 18:15:42 2024
Construct a list of numbers from 1 to 100 using lambda function .
@author: santh
"""

x=lambda n : [i for i in range(1,n)]
n=int(input("Enter the value of n : "))
y=x(n)
print(y)
      