# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 22:13:17 2024
Find the length and  words in each line
@author: santh
"""

f=open("project.txt")
x=1
for i in f:
    length=len(i)
    words=i.split()
    print(x,i,"Length : ",length,"Words : ",words)
    x=x+1
f.close()
