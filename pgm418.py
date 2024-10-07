# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 10:53:39 2024
Sum of two numbers using default arguments
@author: santh
"""

class Sof2num():
    __x=None
    __y=None
    __s=None
    
    def __init__(self,x=10,y=20):
        self.__x=x
        self.__y=y
        
    def find(self):
        self.__s=self.__x + self.__y
        
    def display(self):
        print(self.__s)
        
#main
c=Sof2num()
c.find()
c.display()

d=Sof2num(30)
d.find()
d.display()

e=Sof2num(100,200)
e.find()
e.display()

m=Sof2num(y=500)
m.find()
m.display()

p=Sof2num(y=40,x=50)
p.find()
p.display()