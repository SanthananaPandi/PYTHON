# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 10:21:06 2024
Print the stars in a menu function
@author: santh
"""

def menu():
    print("1.cone")
    print("2.Box")
    print("3.Trai")
    print("4.Right")
    print("5.Pasc")
    print("6.Diamond")
    print("7.num")
    print("8.Alpha")
    print("9.oracle")
    print("10.Boxx")
    print("11.Over")
    n=int(input("Enter the value of n : "))
    return n 

def cone(n):
    for i in range(n):
        print("*" * i)
    for j in range(n,0,-1):
        print("*" * j)

def Box(n):
    for i in range(n,0,-1):
        print("*" * i)
    for j in range(2,n+1):
        print("*" * j)

def Right(n):
    for i in range(n):
        print(" " * i+"*" * (n-i))
    for j in range(2,n+1):
        print(" " * (n-j)+"*" * j)
        
def Trai(n):
    for i in range(1,n):
        print(" " * (n-i)+"*" * i)
    for j in range(n,0,-1):
        print(" " * (n-j)+"*" * j)

def pasc(n):
    for i in range(0,n):
        print(" " * (n-i-1)+"*" * (2*i+1))

def Diamond(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end='')
        for k in range(2*i-1):
            print("*",end='')
        print()

    for i in range(n-1,0,-1):
        for j in range(n-i):
            print(" ",end='')
        for k in range(2*i-1):
            print("*",end='')
        print()

def num(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end='')
        for k in range(1,2*i):
            print(k,end='')
        print()
    
    for i in range(n-1,0,-1):
        for j in range(n-i):
            print(" ",end='')
        for k in range(1,2*i):
            print(k,end='')
        print()
        
def Alpha(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end='')
        for k in range(1,2*i):
            print((chr(96+k)),end='')
        print()
    for i in range(n-1,0,-1):
        for j in range(n-i):
            print(" ",end='')
        for k in range(1,2*i):
            print((chr(96+k)),end='')
        print()

def oracle(n):
    print(" " * n + "*")
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" + " " * (2 * i - 1) + "*")
    print("*" * (2 * n + 1))

def Boxx(n):
    print("*" * (n + 2))
    for i in range(n):
        print("*" + " " * n + "*")
    print("*" * (n + 2))

def over(n):
    print(" " * ((2 * n) + 1) + "*")
    
    for i in range(n - 1):
        print(" " * (2 * n - i) + "*" + " " * (2 * i + 1) + "*")
    
    print(" " * (n + 1) + "*" * (2 * n + 1))
    
    for i in range(n):
        print(" " * (n - i) + "*" + " " * i + "*" + " " * (2 * n - 1) + "*" + " " * i + "*")
    
    for i in range(n - 1, 0, -1):
        print(" " * (n - i + 1) + "*" + " " * (i - 1) + "*" + " " * (2 * n - 1) + "*" + " " * (i - 1) + "*")
    
    print(" " * (n + 1) + "*" * (2 * n + 1))
    
    for i in range(n - 1):
        print(" " * (n + i + 2) + "*" + " " * (2 * (n - 1 - i) - 1) + "*")
    
    print(" " * ((2 * n) + 1) + "*")



#main
x=menu()
while x!=12:
    if x==1:
        n=int(input("Enter the value of n : "))
        cone(n)
    elif x==2:
        n=int(input("Enter the value of n : "))
        Box(n)
    elif x==3:
        n=int(input("Enter the value of n : "))
        Trai(n)
    elif x==4:
        n=int(input("Enter the value of n : "))
        Right(n)
    elif x==5:
        n=int(input("Enter the value of n : "))
        pasc(n)
    elif x==6:
        n=int(input("Enter the value of n : "))
        Diamond(n)
    elif x==7:
        n=int(input("Enter the value of n : "))
        num(n)
    elif x==8:
        n=int(input("Enter the value of n : "))
        Alpha(n)
    elif x==9:
        n=int(input("Enter the value of n : "))
        oracle(n)
    elif x==10:
        n=int(input("Enter the value of n : "))
        Boxx(n)
    elif x==11:
        n=int(input("Enter the value of n : "))
        over(n)
    else:
        pass
    x=menu()
    



         