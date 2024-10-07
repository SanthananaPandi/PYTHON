# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 11:09:34 2024
Derive a point class from A2nos
@author: santh
"""

from pgm422 import A2nos
class point(A2nos):
    pass

#main

c=point()
c.display()

c.setx(50)
c.display()

c.sety(60)
c.display()

c.setxy(100,200)
c.display()

c.reset()
c.display()

d=point()
c.setObject(d)

a=c.getx()
b=c.gety()
d=c.getall()
print(a)
print(b)
print(d)

m=c.getObject()
m.display()
