# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 08:55:54 2024
Accesing three numbers using a protected value
@author: santh
"""

from pgm429 import A2nosPro
class A3nosPro (A2nosPro):
    _z=None
    
    def __init__(self,x=10,y=20,z=30):
        super().__init__(x,y)
        self._z=z
    
    def setz(self,z):
        self._z=z
    
    def setxyz(self,x,y,z):
        self._x=x
        self._y=y
        self._z=z
    
    def reset(self):
        self._x=15
        self._y=25
        self._z=35
        
    def setObject(self,b):
        self._x=b._x
        self._y=b._y
        self._z=b._z
        
    def getz(self):
        return self._z
    
    def getxyz(self):
        return self._x,self._y,self._z
    
    def getObject(self):
        return self
    
    def display(self):
        print(self._x,self._y,self._z)
        
    
#main
c=A3nosPro()
c.display()

c.setz(150)
c.display()

c.setxyz(100,200,500)
c.display()

c.reset()
c.display()

d=A3nosPro()
c.setObject(d)

a=c.getz()
b=c.getxyz()

print(a)
print(b)

m=c.getObject()
m.display()