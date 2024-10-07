# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 10:54:56 2024
Construct a Listbase class using a Scalar operation
@author: santh
"""

from pgm434 import Listbase

class ListScaleOpr(Listbase):
    def __init__(self,a):
        super().__init__(a)
        
    def add(self,v):
        res=[i+v for i in self._a]
        return res
    
    def sub(self,v):
        sub=[i-v for i in self._a]
        return sub
    
    def mul(self,v):
        mul=[i*v for i in self._a]
        return mul
    
    def div(self,v):
        div=[i/v for i in self._a]
        return div
    
    def mod(self,v):
        mod=[i%v for i in self._a]
        return mod
    
    def floor(self,v):
        flo=[i//v for i in self._a]
        return flo
#main
m=ListScaleOpr(10)
m.display()

add=m.add(5)
print(add)

sub=m.sub(5)
print(sub)

mul=m.mul(5)
print(mul)

div=m.div(5)
print(div)

mod=m.mod(5)
print(mod)

floor=m.floor(5)
print(floor)