# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 17:39:11 2024
Segregate the one digit,two digit,three digit and four digits from the set
@author: santh
"""

import random as rd
n=int(input("Enter the value of n : "))
x={rd.randint(-100,10000)for i in range(n)}
y={j for j in x if j>=0 and j<=9}
z={j for j in x if j>=10 and j<=99}
a={j for j in x if j>=100 and j<=999}
b={j for j in x if j>=1000 and j<=9999}
print("Value : ",x)
print("One digit : ",y)
print("Two digit : ",z)
print("Three digit : ",a)
print("Four digit : ",b)