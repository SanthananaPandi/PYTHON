# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 18:40:28 2023
print the stars in form of *****
                            ****
                             ***
                              **
                               *
@author: santh
"""
n=5
a=1
while a<=5:
    b=1
    while b<=n:
        print('*',end='')
        b=b+1
    a=a+1
    n=n-1
    print()
