# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 11:55:45 2024
Count the number of even number and odd number in a list
@author: santh
"""

def num(a):
    b=0
    c=0
    for i in a:
        e=i%2
        if e==0:
            b=b+1
        else:
            c=c+1
    return("Even : ",b,"Odd : ",c)
#main
import random as rd
a=[rd.randint(-100,100)for i in range(100)]
x=num(a)
print(x)