# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 19:11:42 2024
Store a Biodata of n students and print it
@author: santh
"""

d={}
n=int(input("Enter the value of n : "))
for i in range(n):
    Rollno=int(input("Enter the roll : "))
    Name=input("Enter the name : ")
    Age=int(input("Enter the age : "))
    Gender=input("Enter the gender : ")
    Phone=int(input("Enter the phone : "))
    d[Rollno]=[Name,Age,Gender,Phone]

print(d)