# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 10:01:01 2024
print the offset of each line
@author: santh
"""

f=open("pgmfile.txt")
offset=0
x=1
for i in f:
    n=len(i)
    print(x,offset,n,i)
    offset=offset+n
    x=x+1
f.close()