# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 15:34:27 2023
Construct a n list of integers and print it element by element
@author: santh
"""
a=[]
i=0
n=int(input("Enter a value of n: "))
while i<=n-1:
    d=input("Enter the value of d: ")
    a.append(d)
    i=i+1
m=len(a)
j=0
while j<=m-1:
    print(a[j])
    j=j+1
