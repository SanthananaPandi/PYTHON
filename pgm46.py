# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 22:50:52 2023
Given integer number is one,two,three or four digit number using elif
@author: santh
"""
a=int(input("Enter the value of a "))
if a>=0 and a<=9:
    print(a,"is a one digit number")
elif a>=10 and a<=99:
    print(a,"is a two digit number")
elif a>=100 and a<=999:
    print(a,"is a three digit number")
elif a>=1000 and a<=9999:
    print(a,"is a four digit number")
else:
    print("It is not an one,two,three, or a four digit number")    
            