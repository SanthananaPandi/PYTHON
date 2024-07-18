# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 11:21:56 2024
Find out the no.of unique words and print the unique words in the file.
@author: santh
"""

f=open("myy.txt")
x=f.read()
l=x.split()
y=set(l)
n=len(y)
print("No of unique words : ",n,",""unique words : ",y)

