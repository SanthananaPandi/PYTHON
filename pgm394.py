# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 10:16:50 2024
Find out the highest occurence number.
@author: santh
"""

import pickle
f=open('pic','rb')
x=pickle.load(f)
y=set(x)
d={}
for i in y:
    z=x.count(i)
    d[i]=z
    
big=0
for j in d:
    if d[j] > big:
        b=d[j]
        h=j
print(h,b)