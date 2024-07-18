# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 21:38:33 2024
Display the marksheet using a menu function.
@author: santh
"""

def menu():
    print("1.Individual student Marksheet")
    print("2.Consolidation Marksheet of all the students")
    print("3.Passed student List ")
    print("4.Failed student List")
    print("5.Extract Particular student Marksheet")
    print("6.Exit")
    n=int(input("Enter the value of n : "))
    return n

def header():
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

def footer():
    print()
    print("Principle Signature : ")
    print()
    print("Class Teacher Signature       : ")
    print()
    print("_"*110)
    print()

def individual_students():
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
        footer()
        
def consolidation():
    import csv
    f=open("students.csv")
    x=csv.reader(f)
    a=next(x)
    header()
    for i in x:
        for j in range(1,12):
            print(i[j],"\t\t",end='')
        print("_"*110)
        print()
    footer()
    
def passed():
    import csv
    f=open("students.csv")
    x=csv.reader(f)
    a=next(x)
    header()
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
    footer()
    
def failed():
    import csv
    f=open("students.csv")
    x=csv.reader(f)
    a=next(x)
    header()
    for i in x:
        tamil = i[4]
        english = i[5]
        maths = i[6]
        physics = i[7]
        chemistry = i[8]
        if tamil < '35' or english < '35' or maths < '35' or physics < '35' or chemistry < '35':
            for j in range(1, 12):
                print(i[j], "\t\t", end='')
            print()
            print("_"*110)
            print()
    footer()

def particular():
    import csv
    f=open("students.csv")
    x=csv.reader(f)
    a=next(x)
    name=input("Enter the name of the student : ")
    print()
    header()
    for i in x:
        if i[2]==name:
            for j in range(1, 12):
                print(i[j], "\t\t", end='')
            print()
            print("_"*110)
            print()
    footer()
    
#main
x=menu()
while x!=6:
    if x==1:
        individual_students()
    elif x==2:
        consolidation()
    elif x==3:
        passed()
    elif x==4:
        failed()
    elif x==5:
        particular()
    elif x==6:
        pass
    x=menu()