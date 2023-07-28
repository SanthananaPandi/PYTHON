# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 19:20:10 2023
Sum the digits of three numbers
@author: santh
"""
a=int(input("Enter the value of a "))
x=a%10
y=a//10
z=y%10
w=y//10
b=x*100
c=z*10
d=w*1
e=b+c+d
print(e)
