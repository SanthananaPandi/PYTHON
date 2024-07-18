# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 17:58:27 2024
Extract the particular student marksheet.
@author: santh
"""

import csv
f=open("students.csv")
x=csv.reader(f)
a=next(x)
name=input("Enter the name of the student : ")
print()
print("School name :        " , "St.james Matriculation Hr.Sec School")
print()
print("District :           " , "Trichy")
print()
print("Department :         " ,"Bio Informatics")
print()
print("Class Teacher :      " ,"Varun")
print()
print("_"*110)
print()
print("Roll no\t   ","Name\t  ","Mobile Number  ","Tamil ","English ","Maths ","Physics","Chemistry","Total    ","Result   ","Percentage")
print()
print("_"*110)
print()

for i in x:
    if i[2]==name:
        for j in range(1, 12):
            print(i[j], "\t\t", end='')
        print()
        print("_"*110)
        print()
print()
print("Principle Signature : ")
print()
print("Class Teacher Signature       : ")
print()
print("_"*110)
print()
