# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 18:19:35 2024
Read first five line of the text file.
@author: santh
"""

f=open("project.txt")
x=f.readline()
y=f.readline()
z=f.readline()
a=f.readline()
b=f.readline()
print(x)
print(y)
print(z)
print(a)
print(b)
f.close()