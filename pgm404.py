# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 16:56:38 2024
Display only the passed students.
@author: santh
"""

import csv
f=open("students.csv")
x=csv.reader(f)
a=next(x)
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
    tamil = i[4]
    english = i[5]
    maths = i[6]
    physics = i[7]
    chemistry = i[8]
    if tamil >= '35' and english >= '35' and maths >= '35' and physics >= '35' and chemistry >= '35':
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
