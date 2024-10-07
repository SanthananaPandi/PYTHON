# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 18:31:32 2024
Product of two numbers using constructor
@author: santh
"""

class P2num():
    __x=None
    __y=None
    __p=None
    
    def __init__(self):
        self.__x=10
        self.__y=11
        
    def find(self):
        self.__p=self.__x * self.__y
    
    def display(self):
        print(self.__p)
        
#main
c=P2num()
c.find()
c.display()
