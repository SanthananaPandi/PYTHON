# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 18:35:08 2024
Biggest of three numbers using constructor
@author: santh
"""

class Bigof3num():
    __x=None
    __y=None
    __z=None
    __b=None
    
    def __init__(self):
        self.__x=50
        self.__y=150
        self.__z=70
        
    def find(self):
        self.__b=(self.__x if self.__x>self.__z else self.__z) if self.__x>self.__y else(self.__y if self.__y > self.__z else self.__z)
    
    def display(self):
        print(self.__b)
        
#main
c=Bigof3num()
c.find()
c.display()
