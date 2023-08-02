# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 19:11:31 2023
Print the stars in the form of *****
                               ****
                               ***
                               **
                               *
                               **
                               ***
                               ****
                               *****
@author: santh
"""
n=5
a=1
while a<=5:
    b=1
    while b<=n:
        print("*",end='')
        b=b+1
    a=a+1
    n=n-1
    print()
m=2
c=1
while c<=5:
    d=1
    while d<=m:
        print("*",end='')
        d=d+1
    c=c+1
    m=m+1
    print()

