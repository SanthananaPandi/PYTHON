# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 19:20:11 2023
print the * for 5 lines
@author: santh
"""
n=int(input("Enter the value of n: "))
a=1
while a<=5:
    b=1
    while b<=n:
        print("*",end='')
        b=b+1
    a=a+1
    n=n+1
    print()
        
       