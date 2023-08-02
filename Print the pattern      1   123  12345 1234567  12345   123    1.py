# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 18:47:36 2023
Print the pattern  
   1
  123
 12345
1234567
 12345
  123
   1
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
        print(c,end="")
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
        print(c,end="")
        c=c+1
    print()
    a=a+1
    n=n+1
    m=m-2

