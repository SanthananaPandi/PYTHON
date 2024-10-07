# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 11:04:55 2024
Biggest of three numbers using setter and getter function
@author: santh
"""

class Bigof3num():
    __x=None
    __y=None
    __z=None
    __b=None
    
    def __init__(self,x=10,y=20,z=50):
        self.__x=x
        self.__y=y
        self.__z=z
        
    def find(self):
        self.__b=(self.__x if self.__x>self.__z else self.__z) if self.__x>self.__y else(self.__y if self.__y > self.__z else self.__z)
        
    def display(self):
        print(self.__b)
        
    def set_x(self,x):
        self.__x = x
        
    def set_y(self,y):
        self.__y =y
        
    def set_z(self,z):
        self.__z = z
        
    def set_xyz(self,x,y,z):
        self.__x = x
        self.__y = y
        self.__z = z
        
    def reset(self):
        self.__x = 1500
        self.__y = 2500
        self.__z = 3500
        
    def setobject(self,a):
        self.__x = a.__x 
        self.__y = a.__y
        self.__z = a.__z
        
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def get_z(self):
        return self.__z
    
    def get_b(self):
        return self.__b
    
    def getall(self):
        return self.__x,self.__y,self.__z,self.__b
    
    def getobject(self):
        return self
    
        
        
#main
c=Bigof3num()
c.find()
c.display()

c.set_x(650)
c.find()
c.display()

c.set_y(800)
c.find()
c.display()

c.set_z(920)
c.find()
c.display()

c.set_xyz(1000,2000,3000)
c.find()
c.display()

c.reset()
c.find()
c.display()

d=Bigof3num()
c.setobject(d)

a=c.get_x()
l=c.get_y()
e=c.get_z()
f=c.get_b()
g=c.getall()

print(a)
print(l)
print(e)
print(f)
print(g)

m=c.getobject()
m.find()
m.display()
