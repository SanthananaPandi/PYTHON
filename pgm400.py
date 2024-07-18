# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 10:31:35 2024
Print the individual marksheet in a vertical.
@author: santh
"""

import csv
f=open("students.csv")
x=csv.reader(f)
a=next(x)
list=[]
for i in a:
    m=i
    list.append(m)

for i in x:
    p=0
    for y in i:
        print(list[p],y)
        p=p+1
                
