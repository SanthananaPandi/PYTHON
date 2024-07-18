# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 18:49:22 2024
Load the entire binary file and display it.
@author: santh
"""

import random as rd
import pickle
n=int(input("Enter the value of n : "))
l=[rd.randint(-100,100)for i in range(n)]
f=open('pic','wb')
pickle.dump(l,f)
f.close()

f=open('pic','rb')
x=pickle.load(f)

print(x)
f.close()