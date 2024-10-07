# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:37:05 2024
Accesing two numbers using a point operation (protected)
@author: santh
"""

from pgm429 import A2nosPro

class Pointopr(A2nosPro):
    
    def __init__(self,x=10,y=20):
        self._x=x
        self._y=y
    
    def MoveRight(self,dx):
        self._x+= dx
    
    def MoveLeft(self,dx):
        self._x-= dx
    
    def MoveUp(self,dy):
        self._y+=dy
    
    def MoveDown(self,dy):
        self._y-=dy
        
    def MoveRandom(self,dx,dy):
        self._x+=dx
        self._y+=dy
        
        
#main
c=Pointopr()
c.display()

c.MoveRight(10)
c.display()

c.MoveLeft(30)
c.display()

c.MoveUp(100)
c.display()

c.MoveDown(250)
c.display()

c.MoveRandom(100,200)
c.display()