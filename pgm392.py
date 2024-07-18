# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 19:24:35 2024
Find the average,biggest and smallest of a file.
@author: santh
"""
import pickle
f=open('pic','rb')
x=pickle.load(f)

average=sum(x)/len(x)
largest=max(x)
smallest=min(x)
print(x)
print("Largest : ",largest)
print("Smallest : ",smallest)
print("Average : ",average)
