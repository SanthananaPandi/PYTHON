# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 18:41:48 2024
Display the lines between two line numbers.
@author: santh
"""

f=open("myy.txt")
offset=0
line=1
d={}
for i in f:
    n=len(i)
    d[line]=i
    offset=offset+n+1
    line=line+1
a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b :"))
for i in range(a,b):
    print(d[i],end='')
f.close()