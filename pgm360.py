# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 11:59:13 2024
Count the no.of single,two,three,four aand five digits in a list using a map function
@author: santh
"""

def lis(a):
    b=0
    c=0
    d=0
    e=0
    t=0
    for i in a:
        if i>=0 and i<=9:
            b=b+1
        elif i>=10 and i<=99:
            c=c+1
        elif i>=100 and i<=999:
            d=d+1
        elif i>=1000 and i<=9999:
            e=e+1
        elif i>=10000 and i<=99999:
            t=t+1
        else:
            pass
    return("Single :",b,"Two :",c,"Three :",d,"Four :",e,"Five :",t)
#main
import random as rd
a=[rd.randint(1,100000)for i in range(1000)] 
x=lis(a)
print(x)   