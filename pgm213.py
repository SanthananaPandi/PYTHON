# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 11:21:48 2023
Construct a N list of integers and print it element by element
@author: santh
"""
a=[]
n=int(input("Enter the value of n: "))
for i in range(0,n):
    d=input("Enter the value of d: ")
    a.append(d)
for i in a:
    print(i)
