# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 17:06:49 2023
Print the pattern 
* * * * 
 *   *
  * *
   *
@author: santh
"""
a=1
while a<=4:
    print("*",end=' ')
    a=a+1
print()
x=1
y=3
d=1
while d<=2:
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
    d=d+1
    x=x+1
    y=y-2
a=1
while a<=3:
    print(" ",end='')
    a=a+1
print('*')

