# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 18:27:12 2024
Sum of two numbers using constructor
@author: santh
"""

class Sum2num():
    __x=None
    __y=None
    __s=None
    
    def __init__(self):
        self.__x=10
        self.__y=20
        
    def find(self):
        self.__s=self.__x+self.__y
        
    def display(self):
        print(self.__s)

#main
c=Sum2num()
c.find()
c.display()

    