# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 10:13:12 2024
Find the occurence of the each word or a frequency count.
@author: santh
"""

import pickle
f=open('pic','rb')
x=pickle.load(f)
z=set(x)
for i in z:
    y=x.count(i)
    print(i,y)