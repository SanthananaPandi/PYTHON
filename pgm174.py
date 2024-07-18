# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 18:35:12 2023
Print the pattern in the form of  ____*
                                  ___**
                                  __***
                                  _****
                                  *****
@author: santh
"""
k=1
for i in range(4,0,-1):
    print(" " * i + "*" * k)
    k=k+1
print("*" * 5)