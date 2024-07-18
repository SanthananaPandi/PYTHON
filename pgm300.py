# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 17:30:10 2024
Find out the frequency count of the each word
@author: santh
"""

a=[]
s=input("Enter the value of s : ")
a.append(s)
l=s.split()
x=set(l)

for i in x:
    y=l.count(i)
    print(i,y)