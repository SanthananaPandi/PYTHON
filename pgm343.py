# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 11:10:18 2024
Find the allowance of the each employee from their basic pay using map function
@author: santh
"""

def allowance(basic_pay):
    hra_p=hra*(basic_pay / 100)
    cca_p=cca*(basic_pay / 100)
    final=hra_p + cca_p
    return final

#Main
import random as rd
n=int(input("Enter the value of n : "))
hra=int(input("Enter the value of hra : "))
cca=int(input("Enter the value of cca : "))
basic_pay=[rd.randint(20000,200000) for i in range(n)]
x=map(allowance,basic_pay)
print(list(x))
