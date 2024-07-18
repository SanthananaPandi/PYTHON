# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 18:46:21 2024
Generate and dump a list in a binary file.
@author: santh
"""

import random as rd
import pickle
n=int(input("Enter the value of n : "))
l=[rd.randint(1,5000)for i in range(n)]
f=open('pic','wb')
pickle.dump(l,f)
f.close()