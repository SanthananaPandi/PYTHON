# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 11:46:48 2024
Product of two real numbers using oops
@author: santh
"""

class P2realnos():
    __x=None
    __y=None
    __p=None
    
    def set(self):
        self.__x=10.5
        self.__y=11.5
    
    def find(self):
        self.__p= self.__x * self.__y
        
    def display(self):
        print(self.__p)
        
#main

a=P2realnos()
a.set()
a.find()
a.display()