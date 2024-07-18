# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 17:38:23 2024
Find out the higest occurence word in the list
@author: santh
"""

a=[]
s=input("Enter the value of s : ")
a.append(s)
l=s.split()
x=set(l)
d={}
for i in x:
    y=l.count(i)
    d[i]=y
    
b=0
for j in d:
    if d[j]>b:
        b=d[j]
        h=j
    else:
        pass
print(h,b)