# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 11:42:45 2024
Find the detection of the each employee from their basic pay using map function
@author: santh
"""

def detection(basic_pay):
    insurance=insurance_amt*(basic_pay / 100)
    pf_amt=pf*(basic_pay / 100)
    sum= insurance + pf_amt
    return sum

#Main
import random as rd
n=int(input("Enter the value of n : "))
insurance_amt=int(input("Enter the value of insurance amount : "))
pf=int(input("Enter the value of pf : "))
basic_pay=[rd.randint(20000,200000) for i in range(n)]
x=map(detection,basic_pay)
print(list(x))
