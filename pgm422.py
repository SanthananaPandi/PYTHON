# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 23:22:43 2024
Accessing two numbers
@author: santh
"""

class A2nos():
    __x=None
    __y=None
    
    def __init__(self,x=10,y=20):
        self.__x = x
        self.__y = y
        
    def setx(self,x):
        self.__x = x
        
    def sety(self,y):
        self.__y = y
    
    def setxy(self,x,y):
        self.__x = x
        self.__y = y
        
    def reset(self):
        self.__x = 78
        self.__y = 79
        
    def setObject(self,a):
        self.__x = a.__x 
        self.__y = a.__y
        
    def getx(self):
        return self.__x
    
    def gety(self):
        return self.__y
    
    def getall(self):
        return self.__x,self.__y
    
    def getObject(self):
        return self
    
    def display(self):
        print(self.__x,self.__y)
        
#main
c=A2nos()
c.display()

c.setx(50)
c.display()

c.sety(60)
c.display()

c.setxy(100,200)
c.display()

c.reset()
c.display()

d=A2nos()
c.setObject(d)

a=c.getx()
b=c.gety()
d=c.getall()
print(a)
print(b)
print(d)

m=c.getObject()
m.display()

