# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 10:46:44 2024
Print the file in the reverse order
@author: santh
"""

f=open("myy.txt")
offset=0
line=1
d={}
for i in f:
    n=len(i)
    d[line]=[offset,n,i]
    offset=offset+n+1
    line=line+1
for i in range(line-1,0,-1):
    f.seek(d[i][0])
    x=f.readline()
    print(x,end='')
f.close()

