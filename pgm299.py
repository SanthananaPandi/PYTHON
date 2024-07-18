# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 18:59:44 2024
Find out the  percentage of the unique words of given string
@author: santh
"""

a=[]
s=input("Enter the value of s : ")
a.append(s)
l=s.split()
x=set(l)
total=len(l)
unique=len(x)
percentage=(unique/total)*100
print("Given : ",a)
print("Unique : ",x)
print("Percentage : ",percentage)
