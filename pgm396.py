# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 10:32:43 2024
Find out the frequency count of each word.
@author: santh
"""

import pickle
f=open('pic','rb')
x=pickle.load(f)
y=set(x)
for i in y:
    z=x.count(i)
    print(i,z)