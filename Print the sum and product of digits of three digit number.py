# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 19:24:51 2023
Print the sum and product of digits of three digit number
@author: santh
"""
a=int(input("Enter the value of a "))
b=a%10
c=a//10
d=c%10
e=c//10
s=b+d+e
p=b*d*e
print(s)
print(p)
