# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 18:35:06 2023
Print the pattern      *******
                        *   *
                         * *
                          *          
@author: santh
"""
x=3
print("*" * 7)
for i in range (1,3):
    print(" " * i + "*" + " " * x + "*")
    x=x-2
print(" " * 3 + "*")
