# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 17:51:20 2024
Build a Simple calculator using six functions.
@author: santh
"""

def calculator(a,b,opr):
    def sum():
        s=a+b
        return s
    def min():
        s=a-b
        return s
    def pro():
        s=a*b
        return s
    def div():
        s=a/b
        return s
    def flo():
        s=a//b
        return s
    def mod():
        s=a%b
        return s
    
    if opr=='+':
        return sum()
    elif opr=='-':
        return min()
    elif opr=='*':
        return pro()
    elif opr=="/":
        return div()
    elif opr=='//':
        return flo()
    elif opr=='%':
        return mod()
    
#main
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
opr=input("Enter the operator : ")
y=calculator(a,b,opr)
print(y)