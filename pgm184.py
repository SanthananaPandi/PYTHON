# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 19:02:33 2023
Print the pattern               *
                               * *
                              *   *
                             *     *
                            *********
@author: santh
"""

print(" " * 4 +"*")
x=1
for i in range(3,0,-1):
    print(" " * i + "*" + " " * x + "*") 
    x=x+2
print("*" * 9)
