# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 18:38:44 2023
Print the pattern               *
                               * *
                              *   *
                             *     *
                              *   *
                               * *
                                *
 
@author: santh
"""
print(" " * 4 + "*")
x=1
for i in range(3,0,-1):
        print(" " * i + "*" + " " * x + "*")
        x=x+2

y=3
for i in range(2,4):
    print(" " * i + "*" + " " * y + "*")
    y=y-2
print(" " * 4 + "*")
