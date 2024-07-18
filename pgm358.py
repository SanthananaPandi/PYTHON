# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 11:47:02 2024
Count the number of upper,lower,digits and special characters in a given text
@author: santh
"""

def display(a):
    b=0
    c=0
    d=0
    e=0
    for i in a:
        if i>='A' and i<='Z':
            b=b+1
        elif i>='a' and i<='z':
            c=c+1
        elif i>='0' and i<='9':
            d=d+1
        else:
            e=e+1
    return("upper :" ,b,"lower :",c,"digits: ", d,"special:", e)
#main
a=input("Enter the value of a : ")
x=display(a)
print(x)