# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:30:34 2024
Find Biggest of three integers using function within the function
@author: santh
"""

def calculate():
    def big(a,b,c):
        x=(a if a>c else c)if a>b else(b if b>c else c)
        return x
    a=int(input("Enter the value of a : "))
    b=int(input("Enter the value of b : "))
    c=int(input("Enter the value of c : "))
    x=big(a,b,c)
    print(x)
    
#main
calculate()