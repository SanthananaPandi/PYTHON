# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 18:56:47 2024
Store a Biodata roll no as a key using keyboard
@author: santh
"""

d={}
Name=input("Enter the name : ")
Age=int(input("Enter the age :"))
Gender=input("Enter the gender : ")
Phone=int(input("Enter the phone : "))
Rollno=int(input("Enter the roll :"))

d[Rollno]=[Name,Age,Gender,Phone]
print(d)