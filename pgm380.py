# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 18:19:16 2024
Display the alternative lines of the file.
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
for i in range(1,line,2):
    f.seek(d[i][0])
    x=f.readline()
    print(x,end='')
f.close()


