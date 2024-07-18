# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 11:56:53 2024
Print the consolidation marksheet for all the students.
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
    for j in range(1,12):
        print(i[j],"\t\t",end='')
    print("_"*110)
    print()
print()
print("Principle Signature : ")
print()
print("Class Teacher Signature       : ")
print()
print("_"*110)
print()