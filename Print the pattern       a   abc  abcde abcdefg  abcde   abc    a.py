# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 16:24:04 2023
Print the pattern   
   a
  abc
 abcde
abcdefg
 abcde
  abc
   a
@author: santh
"""
x=3
y=1
a=1
while a<=4:
    b=1
    while b<=x:
        print(" ",end="")
        b=b+1
    c=1
    while c<=y:
        print((chr(96+c)),end='')
        c=c+1
    print()
    a=a+1
    x=x-1
    y=y+2
n=1
m=5
a=1
while a<=3:
    b=1
    while b<=n:
        print(" ",end="")
        b=b+1
    c=1
    while c<=m:
        print((chr(96+c)),end="")
        c=c+1
    print()
    a=a+1
    n=n+1
    m=m-2


