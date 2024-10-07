# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 12:07:34 2024
Construct a listbase class
@author: santh
"""

import random as rd
class Listbase():
    _a=[]
    def __init__(self,n=10):
        self._a=[rd.randint(1,100)for i in range(n)]
        
    def __str__(self):
        return ','.join(map(str,self._a))
    
    def display(self):
        print(self._a)
        
#main
m=Listbase()
print(m)
m.display()