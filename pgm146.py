# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:31:37 2023
Construct a 3X3 matrix and print it
@author: santh
"""
c = []
a = 1
while a <= 3:
    b = []
    i = 0
    n = 3
    while i <= n-1:
        d = int(input("Enter the value of d: "))
        b.append(d)
        i = i + 1
    c.append(b)
    a = a + 1
print(c,end='')


