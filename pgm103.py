# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 18:52:53 2023
Print the pattern       *
                       **
                      ***
                     ****
                    *****
                     ****
                      ***
                       **
                        *
@author: santh
"""
n=4
m=1
a=1
while a<=5:
    b=1
    while b<=n:
        print(' ',end="")
        b=b+1
    c=1
    while c<=m:
        print('*',end="")
        c=c+1
    print()
    a=a+1
    n=n-1
    m=m+1
x=1
y=4
c=1
while c<=4:
    d=1
    while d<=x:
        print(" ",end='')
        d=d+1
    e=1
    while e<=y:
        print("*",end='')
        e=e+1
    print()
    c=c+1
    x=x+1
    y=y-1

