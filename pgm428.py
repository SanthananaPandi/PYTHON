# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 10:33:21 2024
Derive operarting a three numbers from A3nos using a constructor
@author: santh
"""

from pgm427 import A3nos

class OP3Nos(A3nos):
    def __init__(self,x=10,y=20,z=30):
        super().__init__(x,y,z)
        
    def summ(self):
        a=self.getx()
        b=self.gety()
        c=self.getz()
        summ=a+b+c
        return summ
    
    def prod(self):
        a=self.getx()
        b=self.gety()
        c=self.getz()
        prod=a*b*c
        return prod
    
    def big(self):
        a=self.getx()
        b=self.gety()
        c=self.getz()
        big=(a if a>c else c) if a>b else (b if b>c else c)
        return big
     
    def small(self):
        a=self.getx()
        b=self.gety()
        c=self.getz()
        small=(a if a<c else c) if a<b else (b if b<c else c)
        return small
    
    
#main
k=OP3Nos()
k.display()

summ=k.summ()
print(summ)

prod=k.prod()
print(prod)

big=k.big()
print(big)

small=k.small()
print(small)

