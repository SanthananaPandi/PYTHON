# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 18:52:38 2024
Find out the precentage of unique and non unique values 
@author: santh
"""

import random as rd
n=int(input("Enter the value of n  : "))
a=[rd.randint(-100,100)for i in range(n)]
x=set(a)

d={}
for i in x:
    y=a.count(i)
    d[i]=y
    
b=[j for j in d if d[j]==1]
c=[j for j in d if d[j]>1]

z=len(b)
r=len(c)
total=len(a)
unique=(z/total)*100
nonunique=(r/total)*100
print("Values : ",d)
print("Unique values : " ,b)
print("Non Unique values : ",c)
print(unique)
print(nonunique)