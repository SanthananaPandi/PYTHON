# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 19:42:31 2024
Biggest of three numbers using default arguments
@author: santh
"""

class Bigof3num():
    __x=None
    __y=None
    __z=None
    __b=None
    
    def __init__(self,x=50,y=150,z=200):
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

m=Bigof3num(100)
m.find()
m.display()

l=Bigof3num(40,500)
l.find()
l.display()

n=Bigof3num(60,850,300)
n.find()
n.display()


