# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:25:27 2024
Construct the random of n integer numbers and count the number of one,two,three,four digits using a global variable.
@author: santh
"""

b=c=d=e=0
def lis(a):
    global b,c,d,e
    for i in a:
        if i>=0 and i<=9:
            b=b+1
        elif i>=10 and i<=99:
            c=c+1
        elif i>=100 and i<=999:
            d=d+1
        elif i>=1000 and i<=9999:
            e=e+1
        else:
            pass
#main
import random as rd
n=int(input("Enter the value of n : "))
a=[rd.randint(1,10000)for i in range(n)]
lis(a)
print("One Digits : ",b)
print("Two Digits : ",c)
print("Three Digits : ",d)
print("Four Digits : ",e)