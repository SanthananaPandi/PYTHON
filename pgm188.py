# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 19:05:57 2023
Print the pattern                     *
                                     * *
                                    *   *
                                   *     *
                                  *********
                                  *       *
                                  *       *
                                  *       *
                                  *       *
                                  *********
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
print("*" * 9)

for i in range(1,5):
    print("*" + " " * 7 + "*")
print("*" * 9)

x=5
for i in range(1,4):
    print(" " * i + "*" + " " * x + "*")
    x=x-2
print(" " * 4 + "*")