# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 18:07:28 2024
Store length of line and words in line and a actual line.
@author: santh
"""

f=open("project.txt")
x=1
d={}
for i in f:
    length=len(i)
    words=i.split()
    d[i]=[length,words,i]
    x=x+1
f.close()
print(d)