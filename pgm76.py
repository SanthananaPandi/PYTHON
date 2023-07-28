# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 22:46:51 2023
Print the years between two limits and find its leap year or not
@author: santh
"""
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
while a<=b:
    d=a%4
    if d==0:
        print("leap year")
    else:
        print("Not")
    print(a)
    a=a+1

