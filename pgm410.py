# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 11:51:57 2024
Area of the circle using oops
@author: santh
"""

class Areaofcircle():
    __r=None
    __a=None
    
    def set(self):
        self.__r=5
        
    def find(self):
        self.__a=22/7 * (self.__r * self.__r)
    
    def display(self):
        print(self.__a)
        
#main
c=Areaofcircle()
c.set()
c.find()
c.display()

        