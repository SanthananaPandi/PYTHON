# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 18:35:55 2023
Print the stars ( *
                  **
                  ***
                  ****
                  ***** )
@author: santh
"""
n=1
a=1
while a<=5:
    b=1
    while b<=n:
        print('*',end='')
        b=b+1
    a=a+1
    n=n+1
    print()