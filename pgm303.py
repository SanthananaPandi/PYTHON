# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 17:41:50 2024
Find out the lowest occurence word in the list
@author: santh
"""

a=[]
s=input("Enter the value of s : ")
a.append(s)
l=s.split()
x=set(l)
d={}
for i in x:
    y=l.count(i)
    d[i]=y
    
b=9999
for j in d:
    if d[j]<b:
        b=d[j]
        h=j
    else:
        pass
print("Word : ",h,"Occurence : ",b)
