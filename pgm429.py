# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 11:14:43 2024
Accesing two numbers using protected(child)
@author: santh
"""

class A2nosPro():
    _x=None
    _y=None
    
    def __init__(self,x=10,y=20):
        self._x=x
        self._y=y
    
    def setx(self,x):
        self._x = x

    def sety(self,y):
        self._y = y
        
    def setxy(self,x,y):
        self._x = x
        self._y = y
    
    def reset(self):
        self._x = 100
        self._y = 200
        
    def setObject(self,a):
        self._x = a._x
        self._y = a._y
        
    def getx(self):
        return self._x
    
    def gety(self):
        return self._y
    
    def getAll(self):
        return self._x,self._y
    
    def getObject(self):
        return self
    
    def display(self):
        print(self._x,self._y)
        
        
#main

c=A2nosPro()
c.display()

c.setx(50)
c.display()

c.sety(100)
c.display()

c.setxy(12,22)
c.display()

c.reset()
c.display()

d=A2nosPro()
c.setObject(d)

a=c.getx()
b=c.gety()
e=c.getAll()

print(a)
print(b)
print(e)

m=c.getObject()
m.display()
