# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 11:05:33 2024
Derive Operating two numbers from A2nos using constructor
@author: santh
"""

from pgm422 import A2nos

class Op2nos(A2nos):
    def __init__(self,x=10,y=20):
        super().__init__(x,y)
    
    def sum(self):
        a=self.getx()
        b=self.gety()
        sum=a+b 
        return sum
    
    def prod(self):
        a=self.getx()
        b=self.gety()
        prod=a*b
        return prod
    
    def quot(self):
        a=self.getx()
        b=self.gety()
        quot=a//b
        return quot
    
    def mod(self):
        a=self.getx()
        b=self.gety()
        mod=a%b
        return mod
    
    def big(self):
        a=self.getx()
        b=self.gety()
        big= a if a>b else b
        return big
    
    def small(self):
        a=self.getx()
        b=self.gety()
        small=a if a<b else b
        return small
    
        
    
#main
c=Op2nos()
c.display()

sum=c.sum()
print(sum)

prod=c.prod()
print(prod)

quot=c.quot()
print(quot)

mod=c.mod()
print(mod)

big=c.big()
print(big)

small=c.small()
print(small)