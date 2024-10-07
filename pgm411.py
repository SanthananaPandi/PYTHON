# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 11:57:38 2024
Biggest of three numbers using oops
@author: santh
"""

class Biggestof3 ():
    __a=None
    __b=None
    __c=None
    __x=None
    
    def set(self):
        self.__a=110
        self.__b=504
        self.__c=503
        
    def find(self):
        self.__x=(self.__a if self.__a>self.__c else self.__c) if self.__a>self.__b else(self.__b if self.__b > self.__c else self.__c)
    
    def display(self):
        print(self.__x)
        
#main
c=Biggestof3()
c.set()
c.find()
c.display()