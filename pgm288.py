# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 15:11:00 2024
Extract only even numbers from already existing set using set comphrension
@author: santh
"""

n=int(input("Enter the value of n : "))
a={int(input("Enter the value : "))for i in range(n)}
b={i for i in a if i%2==0}
print(b)