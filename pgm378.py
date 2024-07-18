# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 08:35:18 2024
Store the offset of text file in a dictionary
@author: santh
"""

f=open("pgmfile.txt")
offset=0
line=1
d={}
for i in f:
    n=len(i)
    d[line]=[offset,n,i]
    offset=offset+n
    line=line+1
f.close()
print(d)