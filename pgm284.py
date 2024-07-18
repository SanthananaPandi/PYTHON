# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 17:58:59 2024
Biggest and Smallest element of the set
@author: santh
"""

a=set()
n=int(input("Enter the value of n : "))
for i in range(n):
    b=int(input("Enter the value of b : "))
    a.add(b)
    
c=0
e=9999
for i in a:
    if i>c:
        c=i
    elif i<e:
        e=i
print(c,"Bigger")
print(e,"Smaller")