# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 23:11:35 2023
Print the pattern  ----*
                   ---**
                   --***
                   -****
                   *****
@author: santh
"""
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 22:53:57 2023

@author: santh
"""
n=4
m=1
a=1
while a<=5:
    b=1
    while b<=n:
        print('-',end="")
        b=b+1
    c=1
    while c<=m:
        print('*',end="")
        c=c+1
    print()
    n=n-1
    a=a+1
    m=m+1
        


