# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 17:34:35 2024
Store the frequency count of the each word in a dictionary
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
print(d)