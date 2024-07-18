# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 17:39:46 2024
Using a offset print the third,second and first line of the file.
@author: santh
"""

f=open("pgmfile.txt")
offset=0
line=1
d={}
for i in f:
    n=len(i)
    d[line]=[offset,n,i]
    offset=offset+n+1
    line=line+1
f.seek(d[3][0])
x=f.readline()
f.seek(d[2][0])
y=f.readline()
f.seek(d[1][0])
z=f.readline()
print(x,end='')
print(y,end='')
print(z,end='')