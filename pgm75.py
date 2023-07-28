# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 22:40:25 2023
Print the number between two limits and find its even or not
@author: santh
"""
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
while a<=b:
    d=a%2
    if d==0:
        print("Even")
    else:
        print("Not")
    print(a)
    a=a+1
