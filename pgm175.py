# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 18:58:20 2023
Print the pattern in the form of  *****
                                  _****
                                  __***
                                  ___**
                                  ____*
@author: santh
"""
n=5
for i in range(0,5,1):
    print("_" * i + "*" * n)
    n=n-1
