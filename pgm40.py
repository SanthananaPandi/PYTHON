# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 19:18:35 2023
Leap year or not
@author: santh
"""
a=int(input("Enter the value of a "))
d=a%4
if d==0:
    print(a,"is a leap year")
else:
    print(a,"is not a leap year")    
