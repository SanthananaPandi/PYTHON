# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 11:47:35 2024
Construct a Listoperator Overriding using a list base class
@author: santh
"""

from pgm434 import Listbase

class ListOprOvr(Listbase):
    def __init__(self,a):
        super().__init__(a)
        
    def __add__(self,a):
        return [i+a for i in self._a]
        
    def __sub__(self,a):
        return [i-a for i in self._a]
    
    def __mul__(self,a):
        return [i*a for i in self._a]
    
    def __truediv__(self,a):
        return [i/a for i in self._a]
        
    def __floordiv__(self,a):
        return [i//a for i in self._a]
        
    def __mod__(self,a):
        return [i%a for i in self._a]
        
#main
m=ListOprOvr(5)
m.display()

add=m+5
print(add)

sub=m-5
print(sub)

mul=m*5
print(mul)

truediv=m/5
print(truediv)

floordiv=m//5
print(floordiv)

mod=m%5
print(mod)