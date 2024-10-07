# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 19:39:12 2024
Area of the circle using default arguments
@author: santh
"""

class Areaofcircle():
    __r=None
    __a=None
    
    def __init__(self,r=5):
        self.__r=r
        
    def find(self):
        self.__a=22/7 * (self.__r * self.__r)
    
    def display(self):
        print(self.__a)
        
#main
c=Areaofcircle()
c.find()
c.display()

m=Areaofcircle(8)
m.find()
m.display()
