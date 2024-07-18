# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 11:08:49 2024
Print the marksheet for a indivudual students.
@author: santh
"""

import csv
f=open("students.csv")
x=csv.reader(f)
a=next(x)
for i in x:
    print("School name :        " , "St.james Matriculation Hr.Sec School")
    print()
    print("District :           " , "Trichy")
    print()
    print("Roll No :            " , i[1])
    print()
    print("Name :               " , i[2])
    print()
    print("Subjects       ","Marks      ","Result")
    print()
    
    for k in range(4,9,1):
        if i[k]>='35':
            r='Pass'
        else:
            r="Fail"
        print(a[k],"\t\t",i[k],"\t\t",r)
        print()
    print("Total           ",i[9])
    print()
    print("Class Teacher Signature : ")
    print()
    print("Parents Signature       : ")
    print()
    print("_"*75)
    print()