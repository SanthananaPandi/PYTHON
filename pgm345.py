# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 11:47:38 2024

@author: santh
"""

def allowance(basic_pay):
    hra_p=hra*(basic_pay / 100)
    cca_p=cca*(basic_pay / 100)
    final=hra_p + cca_p
    return final

def detection(basic_pay):
    insurance=insurance_amt*(basic_pay / 100)
    pf_amt=pf*(basic_pay / 100)
    sum= insurance + pf_amt
    return sum

#Main
import random as rd
n=int(input("Enter the value of n : "))
hra=int(input("Enter the value of hra : "))
cca=int(input("Enter the value of cca : "))
insurance_amt=int(input("Enter the value of insurance amount : "))
pf=int(input("Enter the value of pf : "))
basic_pay=[rd.randint(20000,200000) for i in range(n)]
x=list(map(allowance,basic_pay))
y=list(map(detection,basic_pay))
calculate=[x[i] + y[i] for i in range(n)]
salary=[calculate[i] - basic_pay[i] for i in range(n)]

print("Basic Pay:",basic_pay)
print("Allowance:", x)
print("Detection:", y)
print("Salary:", salary)
