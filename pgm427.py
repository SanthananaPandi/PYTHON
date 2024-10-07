# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 11:12:03 2024
Accesing three numbers using A2nos
@author: santh
"""

from pgm422 import A2nos

class A3nos(A2nos):
    __z = None
    
    def __init__(self, x=10, y=20, z=30):
        super().__init__(x, y)
        self.__z = z
    
    def setz(self, z):
        self.__z = z
        
    def setxyz(self, x, y, z):
        self.setx(x)
        self.sety(y)
        self.__z = z
    
    def reset(self):
        super().reset()
        self.__z = 30
    
    def setobject(self, b):
        super().setObject(b)
        self.__z = b.getz()
    
    def getz(self):
        return self.__z
    
    def getxyz(self):
        return self.__z, super().getall()
    
    def getobject(self):
        return self
    
    def display(self):
        super().display()
        print(self.__z)
    
# main
c = A3nos()
c.display()

c.setz(150)
c.display()

c.setxyz(50, 150, 250)
c.display()

c.reset()
c.display()

d = A3nos()
c.setobject(d)

a = c.getz()
b = c.getxyz()

print(a)
print(b)

m = c.getobject()
m.display()
