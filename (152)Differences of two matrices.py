# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 19:23:18 2023
Difference of two Matrixces
@author: santh
"""
a=[]
b=0
while b<3:
    c=[]
    d=0
    while d<3:
        e=int(input("Enter the value of e: "))
        c.append(e)
        d=d+1
    a.append(c)
    b=b+1

k=[]
i=0
while i<3:
    y=[]
    j=0
    while j<3:
        l=int(input("Enter the value of l: "))
        y.append(l)
        j=j+1
    k.append(y)
    i=i+1

q=[]
x=0
while x<3:
    v=[]
    f=0
    while f<3:
        m=a[x][f]-k[x][f]
        v.append(m)
        f=f+1
    q.append(v)
    x=x+1
print(q)


