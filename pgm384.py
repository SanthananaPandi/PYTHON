# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 11:36:29 2024
Find out the frequency count of the unique words in the file.
@author: santh
"""

f=open("myy.txt")
x=f.read()
l=x.split()
y=set(l)

for i in y:
    m=l.count(i)
    print(i,m)