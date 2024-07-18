# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 19:32:20 2023
Print the pattern  ____*
                   ___**
                   __***
                   _****
                   *****
                   _****
                   __***
                   ___**
                   ____*
                   
@author: santh
"""
k=1
for i in range(4,0,-1):
    print("_" * i +"*" * k)
    k=k+1
n=5
for i in range(0,5):
    print("_" * i + "*" * n)
    n=n-1