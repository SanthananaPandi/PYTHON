# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 19:29:51 2023
Print the pattern      a
                      abc
                     abcde
                    abcdefg
                     abcde
                      abc
                       a
@author: santh
"""
x=1
for i in range(1,5):
    for j in range(4,i,-1):
        print(" ",end=' ')
    for k in range(1,x+1):
        print((chr(96+k)),end=" ")
    print()
    x=x+2

x=5
for i in range(1,4):
    for j in range(1,i+1):
        print(" ",end=' ')
    for k in range(1,x+1):
        print((chr(96+k)),end=" ")
    print()
    x=x-2
