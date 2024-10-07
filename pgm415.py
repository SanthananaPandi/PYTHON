# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 19:27:42 2024
Sum of two number using default arguments
@author: santh
"""

class S2nos():
    __x=None
    __y=None
    __s=None
    
    def __init__(self,x=100,y=200):
        self.__x=x
        self.__y=y
    
    def find(self):
        self.__s= self.__x + self.__y
        
    def display(self):
        print(self.__s)
        
#main
c=S2nos()
c.find()
c.display()

m=S2nos(350)
m.find()
m.display()

l=S2nos(350,700)
l.find()
l.display()


