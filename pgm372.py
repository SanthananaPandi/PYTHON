# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 18:43:17 2024
Display the file along with a line number
@author: santh
"""

f=open("project.txt")
x=1
for i in f:
    print(x,i,end='')
    x=x+1
f.close()