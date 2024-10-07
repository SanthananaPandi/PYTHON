# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 11:01:22 2024
Biggest of three numbers using default arguments
@author: santh
"""

class Bigof3num():
    __x=None
    __y=None
    __z=None
    __b=None
    
    def __init__(self,x=10,y=20,z=30):
        self.__x=x
        self.__y=y
        self.__z=z
        
    def find(self):
        self.__b=(self.__x if self.__x>self.__z else self.__z) if self.__x>self.__y else(self.__y if self.__y > self.__z else self.__z)
    
    def display(self):
        print(self.__b)
        
#main
c=Bigof3num()
c.find()
c.display()

d=Bigof3num(40)
d.find()
d.display()

e=Bigof3num(100,500)
e.find()
e.display()

f=Bigof3num(1000,500,2000)
f.find()
f.display()

g=Bigof3num(y=400)
g.find()
g.display()

h=Bigof3num(z=90,y=40)
h.find()
h.display()

k=Bigof3num(y=11,z=100,x=90)
k.find()
k.display()