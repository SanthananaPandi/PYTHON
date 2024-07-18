# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 17:46:24 2024
Percentage of the different digits of the sets
@author: santh
"""

import random as rd
n=int(input("Enter the value of n : "))
x={rd.randint(-1,10000)for i in range(n)}
y={j for j in x if j>=0 and j<=9}
z={j for j in x if j>=10 and j<=99}
a={j for j in x if j>=100 and j<=999}
b={j for j in x if j>=1000 and j<=9999}
values=len(x)
d=len(y)
e=len(z)
f=len(a)
g=len(b)
one=(d/values)*100
two=(e/values)*100
three=(f/values)*100
four=(g/values)*100
print("Values : ",x)
print("One digit : ",y)
print("Two digit : ",z)
print("Three digit : ",a)
print("Four digit : ",b)
print("Percentage of One digit : ",one)
print("Percentage of Two digit : ",two)
print("Percentage of Three digit : ",three)
print("Percentage of Four digit : ",four)