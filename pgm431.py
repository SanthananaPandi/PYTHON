# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:33:04 2024
Operation on two numbers using A2nospro
@author: santh
"""
from pgm429 import A2nosPro

class Op2nos(A2nosPro):
    
    def __init__(self,x=40,y=20):
        self._x=x
        self._y=y
    
    def summ(self):
        return self._x + self._y
    
    def prod(self):
        return self._x * self._y
    
    def quot(self):
        return self._x // self._y
    
    def mod(self):
        return self._x % self._y
    
    def big(self):
        return self._x if self._x > self._y else self._y
    
    def small(self):
        return self._x if self._x < self._y else self._y
    
#main
c=Op2nos()
c.display()

summ=c.summ()
print(summ)

prod=c.prod()
print(prod)

quot=c.quot()
print(quot)

mod=c.mod()
print(mod)

big=c.big()
print(big)

small=c.small()
print(small)
