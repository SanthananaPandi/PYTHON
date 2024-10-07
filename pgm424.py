# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:08:42 2024
Derive a point class from the A2nos using constructor 
@author: santh
"""

from pgm422 import A2nos
class point(A2nos):
    pass

    def __init__(self,x=10,y=20):
        self.__x=x
        self.__y=y
        
    def display(self):
        print(self.__x,self.__y)
#main
c=point()
c.display()

d=point(15)
d.display()

e=point(150,100)
e.display()

f=point(y=1000)
f.display()

g=point(y=500,x=800)
g.display()