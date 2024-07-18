# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 18:16:20 2024
Segregate the unique value and non unique  value in the list
@author: santh
"""

import random as rd
n=int(input("Enter the value of n : "))
a=[rd.randint(-100,100)for i in range(n)]
x=set(a)

d={}
for i in x:
    y=a.count(i)
    d[i]=y
    
b=[]
c=[]
for j in d:
    if d[j]==1:
        y=j
        b.append(y)
    elif d[j]>1:
        s=j
        c.append(s)
print("Values : ",d)
print("Unique values : " ,b)
print("Non Unique values : ",c)
