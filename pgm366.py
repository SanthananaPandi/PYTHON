# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:12:17 2024

@author: santh
"""

def menu():
    n=int(input("Enter the value of n : "))
    return n
def one(x):
    print("One is : ",x)
def two(x):
    print("Two is : ",x)
def three(x):
    print("Three is : ",x)
def four(x):
    print("Four is : ",x)
def five(x):
    print("Five is : ",x)
        
#main
x=menu()
while x!=6:
    if x==1:
        one(x)
    elif x==2:
        two(x)
    elif x==3:
        three(x)
    elif x==4:
        four(x)
    elif x==5:
        five(x)
    else:
        pass
    x=menu()
        