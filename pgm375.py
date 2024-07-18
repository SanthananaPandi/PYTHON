# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 18:09:58 2024
Display the longest line of the file (using dictionary)
@author: santh
"""

f=open("my.txt")
x=1
d={}
for i in f:
    length=len(i)
    words=i.split()
    d[x]=[length,i,words]
    x=x+1
y=0
for i in d:
    if d[i][0]>y:
        y=d[i][0]
        s=i
f.close()
print(s,d[s][1])