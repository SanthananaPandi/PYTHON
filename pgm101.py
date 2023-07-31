# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 18:39:35 2023
Print the pattern   *****
                    -****
                    --***
                    ---**
                    ----*
@author: santh
"""
n=0#- ku space veika
m=5
a=1
while a<=5:
    b=1
    while b<=n:
        print("-",end='')
        b=b+1
    c=1
    while c<=m:
        print("*",end='')
        c=c+1
    print()
    a=a+1
    m=m-1
    n=n+1
