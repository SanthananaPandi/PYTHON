# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 22:41:30 2023
Given integer number is one,two,three or four digit number
@author: santh
"""
a=int(input("Enter the value of a "))
if a>=0 and a<=9:
    print(a,"is a one digit number")
else:
    if a>=10 and a<=99:
        print(a,"is a two digit number")
    else:
        if a>=100 and a<=999:
            print(a,"is a three digit number")
        else:
            if a>=1000 and a<=9999:
                print(a,"is a four digit number")
            else:
                 print("It is not an one,two,three or four digit number")
