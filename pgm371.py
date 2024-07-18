# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 18:27:24 2024
Read the entire file and display line by line using for loop(iteration)
@author: santh
"""

f=open("project.txt")
for i in f:
    print(i)
f.close()