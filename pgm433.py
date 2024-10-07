# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:49:02 2024
Operation on three numbers uisng protected values
@author: santh
"""

from pgm432 import A3nosPro
class OP3nos(A3nosPro):
    def __init__(self,x=100,y=400,z=300):
        super().__init__(x,y,z)
        
    def summ(self):
        return self._x+self._y+self._z
    
    def prod(self):
        return self._x*self._y*self._z
    
    def quot(self):
        return self._x//self._y//self._z
    
    def mod(self):
        return self._x%self._y%self._z
    
    def big(self):
        return (self._x if self._x > self._y else self._y) if self._x > self._y else(self._y if self._y > self._z else self._z)
    
    def small(self):
        return (self._x if self._x < self._y else self._y) if self._x < self._y else(self._y if self._y < self._z else self._z)



#main
k=OP3nos()
k.display()

summ=k.summ()
print(summ)

prod=k.prod()
print(prod)

quot=k.quot()
print(quot)

mod=k.mod()
print(mod)

big=k.big()
print(big)

small=k.small()
print(small)