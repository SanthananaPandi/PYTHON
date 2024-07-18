# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 10:55:33 2023
Print the pattern               *
                               * *
                              *   *
                             *     *
                            *********
                           **       **
                         *  *       *  *
                       *    *       *    *
                     *      *       *      *
                   *        *       *        *
                 *          *       *          *
                   *        *       *        *
                     *      *       *      *
                       *    *       *    *
                         *  *       *  *
                            *********
                             *     *
                              *   *
                               * *
                                *
@author: santh
"""

print(" " * 18 + "*")
x=1
y=17
for i in range(4,0,-1):
    print(" " * y + "*" + " " * x + "*")
    x=x+2
    y=y-1
print(" " * 13 + "*" * 11)

x=0
y=0
for i in range(12,0,-2):
    print(" " * i + "*" + " " * x + "*" + " " * 9 + "*" + " " * y + "*" )
    y=y+2
    x=x+2
   
x=12
for i in range(0,14,2):
    print(" " * i + "*" + " " * x + "*" + " " * 9 + "*" + " " * x + "*" )
    x=x-2    

print(" " * 13 + "*" * 11)
x=7
y=14
for i in range(1,5):
    print(" " * y + "*" + " " * x + "*")
    x=x-2
    y=y+1
print(" " * 18 + "*")

