# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 09:43:59 2024
Derive an point operation from A2nos using constructor
@author: santh
"""

from pgm422 import A2nos

class Point(A2nos):
    def __init__(self, x=12, y=22):
        super().__init__(x, y)
        
    def setdxdy(self, dx, dy):
        self.__dx = dx
        self.__dy = dy
    
    def Moveright(self, dx):
        cur_x = self.getx()
        right = cur_x + dx
        self.setx(right)
        
    def Moveleft(self, dx):
        cur_x = self.getx()
        left = cur_x - dx
        self.setx(left)
        
    def Moveup(self, dy):
        cur_y = self.gety()
        up = cur_y + dy
        self.sety(up)
        
    def Movedown(self, dy):
        cur_y = self.gety()
        down = cur_y - dy
        self.sety(down)
        
    def Moverandom(self, dx, dy):
        cur_x = self.getx()
        cur_y = self.gety()
        
        rand_x = cur_x + dx
        rand_y = cur_y + dy
        
        self.setx(rand_x)
        self.sety(rand_y)

    def display(self):
        print( self.getx(), self.gety())
        
# main
c = Point()
c.display()

c.setdxdy(50, 100)
c.display()

c.Moveright(20)
c.display()

c.Moveleft(40)
c.display()

c.Moveup(34)
c.display()

c.Movedown(23)
c.display()

c.Moverandom(100, 200)
c.display()
