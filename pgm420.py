# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 19:11:13 2024
Sum of two numbers using setter and getter function.
@author: santh
"""

class S2nos():
    __x=None
    __y=None
    __s=None
    
    def __init__(self,x=10,y=20):
        self.__x=x
        self.__y=y
        
    def find(self):
        self.__s = self.__x + self.__y
        
    def display(self):
        print(self.__s)
        
    def set_x(self,x):
        self.__x = x
    
    def set_y(self,y):
        self.__y = y
        
    def set_xy(self,x,y):
        self.__x = x
        self.__y = y
        
    def reset(self):
        self.__x = 100
        self.__y = 200
        
    def setobject(self,a):
        self.__x = a.__x 
        self.__y = a.__y
        
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def get_s(self):
        return self.__s
    
    def get_all(self):
        return self.__x,self.__y,self.__s
    
    def getobject(self):
        return self
    
    

        
#main
c=S2nos()
c.find()
c.display()

c.set_x(40)
c.find()
c.display()

c.set_y(50)
c.find()
c.display()

c.set_xy(50,60)
c.find()
c.display()

c.reset()
c.find()
c.display()

d=S2nos()
c.setobject(d)

a=c.get_x()
b=c.get_y()
e=c.get_s()
f=c.get_all()
print(a)
print(b)
print(e)
print(f)

y=c.getobject()
y.find()
y.display()

