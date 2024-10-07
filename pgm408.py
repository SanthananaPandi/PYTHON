# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 10:49:31 2024
Sum of two numbers using oops
@author: santh
"""

class S2nos():
    __x=None
    __y=None
    __s=None
    
    def set(self):
        self.__x=10
        self.__y=20
    
    def find(self):
        self.__s=self.__x+self.__y 
        
    def display(self):
        print(self.__s)
        
#main
a=S2nos()
a.set()
a.find()
a.display()