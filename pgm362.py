# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:19:35 2024
Count the number of Upper,Lower,Digits and Special character using a Global variable
@author: santh
"""

b=c=d=e=0
def display(a):
    global b,c,d,e
    for i in a:
        if i>="A" and i<="Z":
            b=b+1
        elif i>="a" and i<="z":
            c=c+1
        elif i>='0' and i<='9':
            d=d+1
        else:
            e=e+1
#main
a=input("Enter the value of a: ")
display(a)
print("Upper case :",b)
print("Lower case : ",c)
print("Digits : ",d)
print("Special characters : ",e)