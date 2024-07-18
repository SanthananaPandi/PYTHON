# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 10:29:27 2024
Find out the unique values of the file.
@author: santh
"""

import pickle
f=open('pic','rb')
x=pickle.load(f)
y=set(x)
print(y)