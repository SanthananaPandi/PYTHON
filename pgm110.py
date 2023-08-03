# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 18:21:57 2023
                       *
Print the pattern     * *
                     *   *
                    *     *
                   *       *
                  ***********
   
@author: santh
"""
a=1
while a<=5:
    print(" ",end='')
    a=a+1
b=1
while b<=1:
    print("*")
    b=b+1
x=4
y=1
a=1
while a<=4:
    b=1
    while b<=x:
        print(" ",end='')
        b=b+1
    print("*",end='')
    c=1
    while c<=y:
        print(" ",end='')
        c=c+1
    print("*")
    a=a+1
    x=x-1
    y=y+2
d=1
while d<=11:
    print("*",end='')
    d=d+1