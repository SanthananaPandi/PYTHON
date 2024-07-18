# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 11:23:21 2024
Load the entire excel sheet into a file and print it.
@author: santh
"""

import csv 
f=open("students.csv")
x=csv.reader(f)
print(x)