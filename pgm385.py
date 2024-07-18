# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 17:40:06 2024
Highest and lowest occurence of word in a file.
@author: santh
"""

f=open("myy.txt")
x=f.read()
l=x.split()
y=set(l)

d={}
for i in y:
    m=l.count(i)
    d[i]=m
    
b=0
c=9999
for j in d:
    if d[j]>b:
        b=d[j]
        h=j
    elif d[j]<c:
        c=d[j]
        k=j
print(h,b)
print(k,c)