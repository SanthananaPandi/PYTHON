# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 19:20:30 2023
Print the pattern         1
                         123
                        12345
                       1234567
                        12345
                         123
                          1
@author: santh
"""
x=1
for i in range(1,5):
    for j in range(4,i,-1):
        print(" ",end=' ')
    for k in range(1,x+1):
        print(k,end=" ")
    print()
    x=x+2
y=5
for i in range(1,4):
    for j in range(1,i+1):
        print(" ",end=' ')
    for k in range(1,y+1):
        print(k,end=" ")
    print()
    y=y-2
    
"""x=1
m=3
for i in range(1,5):
    for j in range(m):
        print(" ",end=' ')
    for k in range(1,x+1):
            print(k,end=' ')
    print()
    x=x+2
    m=m-1
x=5
m=1
for i in range(1,4):
    for j in range(m):
        print(" ",end=" ")
    for k in range(1,x+1):
        print(k,end=" ")
    print()
    x=x-2
    m=m+1"""
    
    
    

    

    
    

    
    